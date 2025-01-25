# Flask-based Fact-Checking System

This project implements a web application for a fact-checking system using Flask, Flask-Login, and SQLAlchemy.

## Repository Structure

```
.
├── app.py
└── extensions.py
```

The repository contains two main files:

- `app.py`: The main entry point of the application, containing the Flask application factory and route definitions.
- `extensions.py`: Likely contains initialization of Flask extensions used in the project.

## Usage Instructions

### Installation

1. Ensure you have Python 3.10 or later installed.
2. Clone this repository.
3. Create a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

To start the application, run:

```
python app.py
```

The application will start in debug mode and can be accessed at `http://localhost:5000`.

### Features

- User authentication (login/logout) using Flask-Login
- Fact submission and management
- Categorization of facts
- Voting system for facts

## Data Flow

1. User sends a request to the Flask application.
2. The request is processed by the appropriate route in `app.py`.
3. If authentication is required, Flask-Login handles the user session.
4. The route may interact with the database using SQLAlchemy models (User, Fact, Category, Vote).
5. The processed data is then rendered in a template and sent back to the user.

```
[User] <-> [Flask App] <-> [SQLAlchemy] <-> [Database]
            |
            v
     [Flask-Login]
```

## Infrastructure

The application uses the following key components:

- Flask: Web framework for handling HTTP requests and responses
- Flask-Login: Manages user sessions and authentication
- SQLAlchemy: ORM for database interactions
- SQLite: Likely used as the database (based on typical Flask setups)

No specific infrastructure files (e.g., Dockerfile, docker-compose.yml) are provided in the given context.