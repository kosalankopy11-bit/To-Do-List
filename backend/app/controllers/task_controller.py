from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.task_model import Task
from app.models.user_model import User
from app.schemas.task_schema import TaskCreate, TaskUpdate


def get_all_tasks(db: Session, current_user: User):
    
    if current_user.is_admin:
        return db.query(Task).all()
    return db.query(Task).filter(Task.user_id == current_user.id).all()


def get_task_by_id(db: Session, task_id: int, current_user: User):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if not current_user.is_admin and task.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You are not the owner of this task")

    return task


def create_task(db: Session, task_data: TaskCreate, current_user: User):
    new_task = Task(
        title=task_data.title,
        description=task_data.description,
        completed=False,
        user_id=current_user.id,
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def update_task(db: Session, task_id: int, task_data: TaskUpdate, current_user: User):
    task = get_task_by_id(db, task_id, current_user)

    if task_data.title is not None:
        task.title = task_data.title
    if task_data.description is not None:
        task.description = task_data.description
    if task_data.completed is not None:
        task.completed = task_data.completed

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int, current_user: User):
    task = get_task_by_id(db, task_id, current_user)
    db.delete(task)
    db.commit()
    return {"message": "Task was deleted (deleted successfully)"}
