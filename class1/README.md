# Poetry Installation and basic commands

To create new project
-> poetry new <project_name>
-> cd <project_name>

To create virtual environment
-> poetry run python --version

If python version is outdated, update it using
-> poetry env use 3.12.4 (or any other version)

To get the environment path
-> poetry env info --path

Copy the path and paste in the python interpreter path in VS Code

To install new packages
-> poetry add <package_name>

To run the project
-> poetry run python ./<project_name>/<filename>.py

## Testing
To run tests
In tests folder create new file with name test_<filename>.py and import the function you want to test
and instead of return statement use assert statement

It uses pytest for testing
-> poetry add pytest
-> poetry run pytest

It will run all the test files in tests folder and tells you if there is any failure