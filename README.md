# FND-Server
Server side code for detecting Fake News text. FND-Client is an android app which will interact with FND-Server to check whether a piece of text is fake. 

# Installation
To use this project follow these steps.

1) Create a virtual environment with the command ```python3 -m venv ANY-NAME-HERE```
2) Turn on the virtual environment.
3) Clone the repository in the virtual environment.
4) Run ``` pip install -r requirements.txt``` to install packages.
5) You also need to have a MySQL database running at 3306 (Check settings.py for more details).
6) Run the project using ```python manage.py runserver```
