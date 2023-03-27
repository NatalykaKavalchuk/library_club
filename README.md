# Library Club

## About:

Django web-app Book Library. 

The main features that have currently been implemented are:

1. There are models for books and authors.
2. Users can view list and detail information for books and authors.
3. Users can add authors and books. It is possible to add an author to an existing book model.



## Quick Start:

To get this project up and running locally on your computer follow the following steps.

1. Clone the repository https://github.com/NatalykaKavalchuk/library_club
2. Set up a python virtual environment
3. Run the following commands

```
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python3 manage.py collectstatic
$ python manage.py createsuperuser
$ python manage.py runserver
```

4. Open a browser and go to http://localhost:8000/
