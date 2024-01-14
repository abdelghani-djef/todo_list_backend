from tortoise.models import Model
from tortoise import fields

class Task(Model):
    """
    Task Model represents a task with a unique identifier, name, and completion status.

    Attributes:
        id (int): Unique identifier for the task (primary key).
        name (str): The name of the task, with a maximum length of 255 characters.
        done (bool): Indicates whether the task is done or not.
    """
    
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    done = fields.BooleanField(
        description="Indicates whether the task is done or not."
    )
