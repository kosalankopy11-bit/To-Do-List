from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.task_model import Task
from app.schemas.task_schema import TaskCreate, TaskUpdate





def get_all_tasks(db: Session):
   return db.query(Task).all()





def get_task_by_id(db: Session, task_id: int):
   task = db.query(Task).filter(Task.id == task_id).first()
   if not task:
       raise HTTPException(status_code=404, detail="Task kidaikala (not found)")
   return task





def create_task(db: Session, task_data: TaskCreate):
   new_task = Task(
       title=task_data.title,
       description=task_data.description,
       completed=False
   )
   db.add(new_task)
   db.commit()
   db.refresh(new_task)  # DB la irundhu latest data (id kooda) edukurathukku
   return new_task





def update_task(db: Session, task_id: int, task_data: TaskUpdate):
   task = get_task_by_id(db, task_id)


   
   if task_data.title is not None:
       task.title = task_data.title
   if task_data.description is not None:
       task.description = task_data.description
   if task_data.completed is not None:
       task.completed = task_data.completed


   db.commit()
   db.refresh(task)
   return task





def delete_task(db: Session, task_id: int):
   task = get_task_by_id(db, task_id)
   db.delete(task)
   db.commit()
   return {"message": "Task delete pannachu (deleted successfully)"}
