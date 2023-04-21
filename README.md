# python_tool_template
A template repository to copy for future python projects.

## Creating a virtual environment
1. Create an environment file named .env and store PIPENV_VENV_IN_PROJECT=1.
2. Create a folder named .venv in the project repository. (It will not be in the template as its included in .gitignore)
3. python -m pipenv install

## Deleting .venv using pipenv
- python -m pipenv --rm

## Activate the virtual environment
- python -m pipenv shell

## Deactivate the virtual environment
- exit

## Running a python file with pipenv (ensures all environment variables are included)
- python -m pipenv run python path/to/python/file.py

## Installing a package 
- python -m pipenv install pandas