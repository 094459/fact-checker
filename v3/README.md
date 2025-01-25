# Fact Check Application

A web application for community-based fact checking. Users can submit facts, provide supporting evidence, and vote on the accuracy of facts submitted by others.

## Features

- User registration and authentication
- Create and categorize facts
- Submit supporting URLs and information
- Vote on fact accuracy
- View voting statistics
- Responsive design

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
- Copy `.env.example` to `.env`
- Update `SECRET_KEY` and `DATABASE_URI` as needed

3. Run the application:
```bash
python app.py
```

4. Access the application at http://localhost:5000

## Usage

1. Register an account or login
2. Create categories for facts
3. Submit new facts with supporting evidence
4. Vote on existing facts
5. View voting statistics for each fact

## Development

The application is built with:

- Flask for the web framework
- SQLAlchemy for database operations
- Flask-Login for user authentication
- SQLite for the database