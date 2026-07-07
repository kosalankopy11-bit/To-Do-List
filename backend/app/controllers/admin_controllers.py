from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException

from app.models.user_model import User
from app.models.task_model import Task


def get_all_users(db: Session):
    users = db.query(User).all()
    result = []
    for user in users:
        task_count = db.query(func.count(Task.id)).filter(Task.user_id == user.id).scalar()
        result.append(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "is_admin": user.is_admin,
                "task_count": task_count,
            }
        )
    return result


def delete_user(db: Session, user_id: int, current_admin: User):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.id == current_admin.id:
        raise HTTPException(status_code=400, detail="You cannot delete yourself")

    db.delete(user)
    db.commit()
    return {"message": f"User '{user.username}' deleted (All tasks have been removed)"}


def get_all_tasks_admin(db: Session):
    tasks = db.query(Task).join(User, Task.user_id == User.id).all()
    result = []
    for task in tasks:
        result.append(
            {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "completed": task.completed,
                "user_id": task.user_id,
                "owner_username": task.owner.username,
            }
        )
    return result


def delete_task_admin(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}