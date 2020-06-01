### LIBRARY MANAGEMENT SYSTEM

Developed in Django==1.10
```
  > sudo apt-get install python3-pip
  > pip3 install virtualenv
  > virtualenv test
  > . test/bin/activate
  # Now you should be in the test virtual environment. 
  #   You can verify this by observing the commandline to be as follows - (test)$username
  > pip install Django==1.10
  > pip install selenium
```
  
To run this project first clone this repo and in the cloned directory run 
```
  > python manage.py makemigrations
  > python manage.py migrate
  > python manage.py createsuperuser // to create a superuser to log in to the website as admin 
  > python manage.py runserver
```
To perform system testing
```
  > python manage.py test libman 
```
And the project will run in https://localhost:8000.
