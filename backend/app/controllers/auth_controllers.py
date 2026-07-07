from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.user_model import User
from app.schemas.user_schema import UserRegister, UserLogin
from app.utils.security import hash_password, verify_password, create_access_token


def register_user(db: Session, user_data: UserRegister) -> User:
    existing_username = db.query(User).filter(User.username == user_data.username).first()
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already exists. please try a different one.")

    existing_email = db.query(User).filter(User.email == user_data.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered. please try a different one.")

   
    is_first_user = db.query(User).count() == 0

    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
        is_admin=is_first_user,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def login_user(db: Session, login_data: UserLogin):
    user = db.query(User).filter(User.username == login_data.username).first()
    if not user or not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username allathu password thappu irukku",
        )

    access_token = create_access_token(
        data={"sub": user.username, "user_id": user.id, "is_admin": user.is_admin}
    )
    return {"access_token": access_token, "token_type": "bearer", "user": user}
