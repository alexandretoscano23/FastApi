import os

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

from routers.auth_routes import auth_router
from routers.order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)
