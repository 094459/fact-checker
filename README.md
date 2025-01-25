## Fact Checker

This repo container a number of versions of a Fact Checking application that was used during a live coding session.

To use them, simply rename the file to "fact-checker" (e.g mv v1 fact-checker) and then you can create/activate a virtual environment, install the dependant libraries (flask, flask-login, flask-sqlalchemy) and run the app by using "python app.py".

All five versions work but have slightly different logic, look n feel, etc.


The prompts and supporting files used where as follows (if you want to try and replicate)

**Creating the Data Model**

> Create a data model for a Fact checking application. Users will be able to register and log in via their email address. During registration a username is also captured (it does not need to be unique). Users will be able to create Facts, which will be text based paragraphs with a supporting URL link (which is optional). Each Fact will have a Category type. Each Fact will keep track of Votes. Votes can either be "Fact" or "Fake". Each Fact will also have an additional text field for supporting info. Generate SQL that will work with sqlite

I output the contents after reviewing and then editing to a file called "data/fact-check.sql"

**Creating a scaffold file**

I create a file called "project-stds/project-stds.md" and add this to it.

```
When creating Python code, use the following guidance

- Use Flask as the web framework
- Follow Flask's application factory pattern
- Use environment variables for configuration
- Implement Flask-SQLAlchemy for database operations

Use the following project structure

├── static/
├── models/
├── routes/
├── templates/
├ extensions.py
├ app.py

```

**Prompt for the /dev agent**

> Build a simple Fact Checking application. 

- Use the data mode in the sql/fact-check.sql
- Generate a web application that can be used in a browser
- Users will need to register with an email address to login
- When Users login, a Dashboard will be displayed that provides a simple explanation of what the application does, and displays any available Facts that have been created
- From the home Dashboard, Users will be able to click on any existing Facts to fact check. They will also be able to Create a new Fact or Create a new Category
- When Users are viewing Facts, they will have the ability to click on two buttons - Fact or Fake
- When Users are viewing Facts, they can also provide supporting info
-  Provide a simple web design that can be updated easily using CSS
-  Review project layout details in project-stds.md
-  Ensure the database is initialised properly