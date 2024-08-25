TaskMasterX API - ALX Africa SE Final Specialization Project written by Augustine Jude, Cohort 18

TaskMasterX API is a task management system built with Flask. It supports user registration, task creation, retrieval, updating, and deletion. The API is designed to be secure, using JWT for authentication and Flask for managing the API endpoints.

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- Docker (optional for containerized deployment)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/TaskMasterX_API.git
   cd TaskMasterX_API
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```bash
   flask db upgrade
   ```

5. Run the application:

   ```bash
   flask run
   ```

   The application will be available at `http://localhost:5003`.

### Usage

#### Authentication

- Register a User:

   ```bash
   curl -X POST http://localhost:5000/register \
   -H "Content-Type: application/json" \
   -d '{"username": "Techlord", "password": "breaklimit"}'
   ```

- Login to get a token:

   ```bash
   curl -X POST http://localhost:5000/login \
   -H "Content-Type: application/json" \
   -d '{"username": "Techlord", "password": "breaklimit"}'
   ```

#### Task Management

- Create a Task:

   ```bash
   curl -X POST http://localhost:5000/tasks \
   -H "Authorization: Bearer <your_token>" \
   -H "Content-Type: application/json" \
   -d '{"title": "New Task", "description": "Task description"}'
   ```

- Get All Tasks:

   ```bash
   curl -X GET http://localhost:5000/tasks \
   -H "Authorization: Bearer <your_token>"
   ```

- Get a Task by ID:

   ```bash
   curl -X GET http://localhost:5000/tasks/<task_id> \
   -H "Authorization: Bearer <your_token>"
   ```

- Update a Task by ID:

   ```bash
   curl -X PUT http://localhost:5000/tasks/<task_id> \
   -H "Authorization: Bearer <your_token>" \
   -H "Content-Type: application/json" \
   -d '{"title": "Updated Task", "description": "Updated description"}'
   ```

- Delete a Task by ID:

   ```bash
   curl -X DELETE http://localhost:5000/tasks/<task_id> \
   -H "Authorization: Bearer <your_token>"
   ```

### Running Tests

To run the tests, use:

```bash
pytest
```

### Docker Setup (Optional)

1. Build the Docker image:

   ```bash
   docker build -t TaskMaster_API .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 5000:5000 TaskMaster_API
   ```

The application will be available at `http://localhost:5003`.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Project Summary

TaskMaster API** is a Flask-based application for managing tasks. The API supports the following features:

1. User Management:
   - Register: Create a new user with a username and password.
   - Login: Authenticate a user and obtain a JWT token for secure access.

2. Task Management:
   - Create: Add a new task with a title and optional description.
   - Retrieve: Get all tasks or a specific task by ID.
   - Update: Modify an existing task's title and description.
   - Delete: Remove a task by its ID.

Technical Stack:
- Backend: Flask
- Database: SQLite (with support for migrations via Flask-Migrate)
- Authentication: JWT (via Flask-JWT-Extended)

Testing: The application includes unit tests using pytest to ensure proper functionality of the endpoints.

Deployment: The project includes a Dockerfile for containerization, enabling easy deployment in various environments.

Setup Instructions: The `README.md` provides step-by-step instructions for setting up the development environment, running the application, and using Docker if desired
