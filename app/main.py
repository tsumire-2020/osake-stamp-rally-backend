from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.api.todo_api import todo_router
from app.api.stamprally_api import stamprally_router


# アプリケーションの設定
app = FastAPI()

api_router = APIRouter()
api_router.include_router(todo_router)
api_router.include_router(stamprally_router)

app.include_router(api_router)

# CORS Setting
origins = [
  "http://localhost:3000"
]
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

