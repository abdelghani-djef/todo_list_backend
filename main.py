"""
FastAPI Task Management Application

This script creates a FastAPI application for managing tasks. It utilizes Tortoise ORM for database operations
and includes a router (task_router) for task-related endpoints. CORS (Cross-Origin Resource Sharing) is configured
to allow cross-origin requests. Database connection details are loaded from environment variables.

Modules:
- FastAPI: Web framework for building APIs with Python.
- Tortoise ORM: Async ORM (Object Relational Mapper) inspired by Django.
- CORS Middleware: Middleware for handling Cross-Origin Resource Sharing.
- dotenv: Library for loading environment variables from a .env file.

"""
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Import the router for tasks
from app.routers.task_router import task_router

# Load environment variables from a .env file
load_dotenv()

# Create a FastAPI application instance
app = FastAPI()

# Define the allowed origins for CORS (Cross-Origin Resource Sharing)
origins = ["*"]

# Configure CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Tortoise ORM with FastAPI
register_tortoise(
    app,
    db_url=os.getenv('DATABASE_URL'),# Get the database URL from environment variables
    modules={'models': ['app.models.task']},# Specify the Tortoise ORM models
    generate_schemas=True,# Generate the database schema
    add_exception_handlers=True,# Add exception handlers for Tortoise ORM
)

# Include the task_router with a specified prefix
app.include_router(task_router, prefix="/task")
