
# People List API

Django API using rest framework and JWT


## Documentation

### API Endpoints
| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | /login/ | To sign in and get tokens access |
| POST | /refresh/ | To refresh access token |
| GET | /user/:userId | To retrieve user information |
| GET | /person/ | To retrieve people list |
| POST | /person/ | To create a person item |
| GET | /person/:personId | To retrieve person item details |
| PUT | /person/:personId | To update person item |
| DELETE | /person/:personId | To delete person item |


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file in project folder ("peopleListProject")

```
SECRET_KEY=

DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=
```


## Installation
Activate the virtualenv for your project.

Install project dependencies:

```bash
  pip install -r requirements.txt
```
    
Run the development server:

```bash
  npm run dev
```

Then simply apply the migrations:

```bash
  python manage.py migrate
```

You can now run the development server:

```bash
  python manage.py runserver
```

## Deploy on Heroku

- https://people-list-api.herokuapp.com/

