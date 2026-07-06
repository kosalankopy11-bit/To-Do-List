from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routes import task_route

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo List App")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_route.router)


@app.get("/")
def read_root():
    return {"message": "Todo List App Backend Server Run Aagudhu!"}
