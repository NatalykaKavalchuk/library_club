# ***Library Club***

## *About:*

A compact web service that allows to work with 'authors' and 'books'.

Technologies used:
- Django: user-friendly interface of project;
- Django Rest Framework (DRF): allows to easily create a REST API of project;
- Swagger: allows anyone to visualize and interact with the API’s resources.  

The main features that have currently been implemented are:

1. There are models for books and authors.
2. The **"Books"** section displays a table of all books from the database. Using the key **"Add book"**, the user can independently add a book to the section. 

![Screenshot of API ](https://github.com/NatalykaKavalchuk/library_club/blob/master/media/pictures/books.jpg?raw=true)

3. It is possible to add an author to an existing book model.

![Screenshot of API ](https://github.com/NatalykaKavalchuk/library_club/blob/master/media/pictures/book_detail.jpg?raw=true) 
 
4. The **"Authorss"** section displays a table of all authors from the database. You can get detailed information about each author, including all his books. Added the ability to add an author to the database using  **"Add author"**.

![Screenshot of API ](https://github.com/NatalykaKavalchuk/library_club/blob/master/media/pictures/authors.jpg?raw=true) 

5. The API allows you to add, delete, make partial or complete changes to existing data about the book/author. 

![Screenshot of API ](https://github.com/NatalykaKavalchuk/library_club/blob/master/media/pictures/api.jpg?raw=true) 

6. The ability to add posters for books and photos for authors is implemented only through the base django application.
7. CI/CD pipeline is configured based on GitHub Actions.

## *Quick Start:*

To get this project up and running locally on your computer follow the following steps.

1. Clone the repository https://github.com/NatalykaKavalchuk/library_club
2. Set up a python virtual environment `$ python -m venv venv`
3. Run the following commands

```
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py createsuperuser
$ python manage.py runserver
```

4. Open a browser and go to http://localhost:8000/
5. You can also work with the app using swagger-ui http://127.0.0.1:8000/api/swagger-ui/


