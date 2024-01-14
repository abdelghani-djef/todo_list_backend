from fastapi import APIRouter, HTTPException
from typing import List
from app.models.task import Task
from tortoise.contrib.pydantic import pydantic_model_creator

# Create an instance of APIRouter
task_router = APIRouter()

# Create Pydantic models
Task_Pydantic = pydantic_model_creator(Task, name='Task')
Task_Display_Pydantic = pydantic_model_creator(
    Task,
    name='Task Client',
    exclude_readonly=True,
)

@task_router.get("/all", response_model=List[Task_Pydantic])
async def read_all_tasks():
    """
    Read all tasks.

    Returns:
        List[Task_Pydantic]: A list of tasks.
    """
    tasks = await Task_Pydantic.from_queryset(Task.all())
    return tasks

@task_router.post("", status_code=201)
async def create_task(task: Task_Display_Pydantic):
    """
    Create a new task.

    Args:
        task (Task_Display_Pydantic): The task to be created.

    Returns:
        Task_Pydantic: The created task.
    """
    return await Task.create(**task.dict())

@task_router.get("/{task_id}", response_model=Task_Pydantic)
async def read_task(task_id: int):
    """
    Read a specific task by its ID.

    Args:
        task_id (int): The ID of the task to be retrieved.

    Returns:
        Task_Pydantic: The retrieved task.

    Raises:
        HTTPException: If the task is not found (status_code=404).
    """
    task = await Task.get_or_none(id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@task_router.put("/{task_id}", response_model=Task_Pydantic)
async def update_task(task_id: int, updated_task: Task_Display_Pydantic):
    """
    Update a task by its ID.

    Args:
        task_id (int): The ID of the task to be updated.
        updated_task (Task_Display_Pydantic): The updated task data.

    Returns:
        Task_Pydantic: The updated task.

    Raises:
        HTTPException: If the task is not found (status_code=404).
    """
    existing_task = await Task.get_or_none(id=task_id)

    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    for field, value in updated_task.dict(exclude_unset=True).items():
        setattr(existing_task, field, value)

    await existing_task.save()
    return existing_task

@task_router.delete("/{task_id}", response_model=dict)
async def delete_task(task_id: int):
    """
    Delete a task by its ID.

    Args:
        task_id (int): The ID of the task to be deleted.

    Returns:
        dict: A message indicating the task is deleted.

    Raises:
        HTTPException: If the task is not found (status_code=404).
    """
    deleted_count = await Task.filter(id=task_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted."}
