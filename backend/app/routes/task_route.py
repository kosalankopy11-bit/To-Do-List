from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List


from app.database import get_db
from app.schemas.task_schema import TaskCreate, TaskUpdate, TaskResponse
from app.controllers import task_controller


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/", response_model=List[TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
   return task_controller.get_all_tasks(db)


@router.get("/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
   return task_controller.get_task_by_id(db, task_id)


@router.post("/", response_model=TaskResponse)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
   return task_controller.create_task(db, task)


@router.put("/{task_id}", response_model=TaskResponse)
def update_existing_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
   return task_controller.update_task(db, task_id, task)


@router.delete("/{task_id}")
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
   return task_controller.delete_task(db, task_id)
