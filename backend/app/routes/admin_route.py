from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.controllers import admin_controller
from app.dependencies import get_current_admin
from app.models.user_model import User

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/users")
def list_all_users(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    return admin_controller.get_all_users(db)


@router.delete("/users/{user_id}")
def remove_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    return admin_controller.delete_user(db, user_id, current_admin)


@router.get("/tasks")
def list_all_tasks(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    return admin_controller.get_all_tasks_admin(db)


@router.delete("/tasks/{task_id}")
def remove_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    return admin_controller.delete_task_admin(db, task_id)
