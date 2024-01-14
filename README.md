# FastAPI Todo List Application - Backend

This repository contains the backend implementation of a simple Todo List application using FastAPI.

## Features

- Create, read, update, and delete tasks.
- Store tasks in a MySQL database.
- RESTful API design.

## Getting Started
### Prerequisites

Make sure you have python 3.7+ installed on your machine.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/todo_list_backend.git

    cd todo_list_backend
    ```

2. Configurations:

    Before running the application, make sure to set up the following environment variables. You can create a `.env` file in the root directory of your project and add the necessary values.

    ```env
    DATABASE_URL=mysql://sql11676445:ugI361zcup@sql11.freemysqlhosting.net:3306/sql11676445
    ```

    That is the connection URL for your MySQL database. Ensure it includes the correct credentials, host, port, and database name.

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

    The application will be accessible at `http://localhost:8000`.

## API Endpoints

- `GET /task/all`: Get a list of all tasks.
- `GET /task/{id}`: Get a specific task.
- `POST /task`: Create a new task.
- `PUT /task/{id}`: Update a task values by id.
- `DELETE /task/{id}`: Delete a task by id.


## Usage

1. Use your preferred API client to interact with the API.
2. Create, update, delete task items using the provided endpoints.

### Task Structure

Each task has the following structure:
- **ID:** A unique identifier for each task.
- **Name:** The name of the task.
- **Done:** A boolean value indicating whether the task is completed or not.

