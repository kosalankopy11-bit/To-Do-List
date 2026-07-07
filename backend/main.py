from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routes import task_route


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo List App")


origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:5175",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_route.router)

@app.get("/")
def read_root():
    return {"message": "Todo List App Backend Server is running!"}
