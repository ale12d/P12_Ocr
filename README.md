# P12_Ocr

## Table of contents
* [General info](#general-info)
* [Packages](#packages)
* [Setup Linux](#setup-linux)
* [Setup Windows](#setup-windows)
* [End points](#end-points)
 
## General info
This project is an API allowing to follow up clients and create their events and contracts in a database.

## Packages
Project is created with:
* asgiref: 3.5.2
* Django: 4.0.5
* djangorestframework: 3.13.1
* pytz: 2022.1
* sqlparse: 0.4.2
* tzdata: 2022.1
* djangorestframework-simplejwt: 5.2.0
* django-cors-headers: 3.13.0
* django-filter: 22.1
* PyJWT: 2.4.0
* urllib3: 1.26.12
* psycopg2: 2.9.3

## Setup Linux
To run this project, install python3 : ```sudo apt install python3.8```

Go in the project folder : ```cd /.../P12_Ocr-main```

Create a virtual environment : ```python3 -m venv env```

Activate the virtual environment : ```source env/bin/activate```

To install directly all packages you need : ```python -m pip install -r requirements.txt```

Create your database: ```python EpicEvents\manage.py makemigrations```
                        +
                      ```python EpicEvents\manage.py migrate```

Run the django server : ```python EpicEvents\manage.py runserver```

To test all end points(optional) : ```python EpicEvents\manage.py test```

## Setup Windows
To run this project, write ```python3``` in the cmd to install python3 in microsoft store

Go in the project folder : ```cd \...\P12_Ocr-main```

Create a virtual environment : ```python3 -m venv env```

Activate the virtual environment : ```\Users\...\P12_Ocr-main\env\Scripts\activate.bat```

To install directly all package you need : ```python -m pip install -r requirements.txt```

Create your database: ```python EpicEvents\manage.py makemigrations```
                        +
                      ```python EpicEvents\manage.py migrate```
                      
Run the django server : ```python EpicEvents\manage.py runserver```

To test end points(optional) : ```python EpicEvents\manage.py test```

## End points

Create User account: http://127.0.0.1:8000/signup

Login (copy access token) : http://127.0.0.1:8000/login

Data:

- http://127.0.0.1:8000/api/clients/

- http://127.0.0.1:8000/api/contracts/

- http://127.0.0.1:8000/api/events/
---
- http://127.0.0.1:8000/api/clients/{nb}/

- http://127.0.0.1:8000/api/contracts/{nb}/

- http://127.0.0.1:8000/api/events/{nb}/
