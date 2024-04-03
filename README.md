# Online Learning Platform API

## Overview

This Django application provides backend services for an online learning platform. It includes API endpoints for managing courses and student enrollments.

## Installation

### Prerequisites

- Python 3.x
- Docker (optional, for running with PostgreSQL)

### Setup

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd online_learning_platform
    ```

3. Install dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin interface:

    ```bash
    python manage.py createsuperuser
    ```

6. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://localhost:8000/`.

### Running with Docker

To run the application with Docker and PostgreSQL, follow these steps:

1. Navigate to the project directory:

    ```bash
    cd online_learning_platform
    ```

2. Start the Docker containers:

    ```bash
    docker-compose up --build
    ```

3. The application will be accessible at `http://localhost:8000/`.

## API Endpoints

### Courses

- **GET /api/courses/**: Retrieve a list of available courses.
- **GET /api/courses/{id}/**: Retrieve details of a specific course by its ID.
- **POST /api/courses/**: Create a new course.

### Enrollments

- **POST /api/enrollments/**: Enroll a student in a course.

## Examples

### Retrieve Courses

Send a GET request to `/api/courses/` to retrieve a list of available courses.

Example:

```bash
curl http://localhost:8000/api/courses/
```

### Create a Course

Send a POST request to `/api/courses/` with JSON data containing course details to create a new course.

Example:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"title": "Data Science Fundamentals", "description": "Explore data science concepts and techniques.", "instructor": "David Brown", "duration": 150, "price": 99.99}' http://localhost:8000/api/courses/
```

## Dependencies

- Django 5.0.3
- Django Rest Framework 3.13.0

## Environment Variables

- `POSTGRES_DB`: Name of the PostgreSQL database (optional, when using Docker)
- `POSTGRES_USER`: PostgreSQL username (optional, when using Docker)
- `POSTGRES_PASSWORD`: PostgreSQL password (optional, when using Docker)

Adjust the values according to your specific requirements and configurations.

---

Feel free to customize this README file based on your specific application details and requirements. Additionally, provide instructions for any additional setup or configuration steps that may be necessary for your specific application environment.
