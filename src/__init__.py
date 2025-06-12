from fastapi import FastAPI 
from src.books.routes import book_router
from src.auth.routes import auth_router
from contextlib import asynccontextmanager 
from src.db.main import init_db


@asynccontextmanager 
async def life_span(app: FastAPI):
    print("Server is started...")
    await init_db()
    yield
    # This code will be executed when the server is stopped
    print("Server has been stoped")

version = "v1"
app = FastAPI(
    title = "Brookly",
    version = version,
    description = "A website for book review web service",
    lifespan = life_span
)

app.include_router(book_router, prefix ="/api/{version}/books", tags=['book']) 
app.include_router(auth_router, prefix="/api/{version}/auth", tags=['auth']) 