## Python Calculator Project
This project is a Python-based interactive calculator that performs basic arithmetic operations (addition, subtraction, multiplication, and division) through a command-line interface (CLI). The application is structured with modular command classes and supports features such as calculation history, environment variable configuration, and extensive logging for improved tracking and debugging.

## Features
- Arithmetic Operations: Supports addition, subtraction, multiplication, and division.
- Calculation History: Maintains a history of all calculations performed during a session.
- Error Handling: Handles exceptions for invalid inputs and division by zero.
- Environment Configuration: Uses environment variables for setting up configuration (e.g., environment type, database username).
- Logging: Logs all operations, errors, and environment details to app.log.

## Installation
Clone the Repository:
 ```bash
git clone https://github.com/your-username/calc_logg_v1.git
cd calc_logg_v1
 ```
## Set Up Virtual Environment:
``` bash
python3 -m venv venv
source venv/bin/activate  # For MacOS/Linux
venv\Scripts\activate     # For Windows
 ```
## Install Dependencies:
``` bash
pip install -r requirements.txt
```
## Set Up Environment Variables:
```bash
environment=development
database_username=root
```
Add .env to .gitignore to prevent sensitive data from being shared in the repository.

## Running the Application
```bash
python3 main.py
```
Available Commands
- add: Add two numbers
- subtract: Subtract two numbers
- multiply: Multiply two numbers
- divide: Divide two numbers
- history: View the history of calculations performed
- clear_history: Clear the calculation history
- menu: Display the list of available commands
- exit: Exit the application

## Logging
Logs are saved to app.log with details about each operation, errors encountered, and environment information. Logging is configured in main.py, and by default, it logs to both the console and the app.log file.

## GitHub Actions
The project includes a CI workflow configured with GitHub Actions. Each push to the main branch triggers the workflow, which runs the tests and checks code quality with pylint.


