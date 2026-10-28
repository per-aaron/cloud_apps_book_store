import sys
import os

from app import app
from database_connection import DatabaseConnection

def test_sessions_accepts_login_data():
    # create the test client to send requests without using Playwright and a browser
    client = app.test_client()

    # set up a DB connection
    connection = DatabaseConnection()
    connection.connect()
    #connection.seed("./seeds/users.sql")
    #Below more appropriate than seeding since it is just one command required
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('testuser', 'password123');")

   # send the request
    response = client.post('/sessions', data={
        'username': 'testuser',
        'password': 'password123'
    })

    # assert that the redirect happened
    assert response.status_code == 302

    # assert that user is redirected to /books
    assert response.headers['Location'].endswith('/books')

def test_sessions_rejects_incorrect_password():
    # create the test client to send requests without using Playwright and a browser
    client = app.test_client()

    # set up a DB connection
    connection = DatabaseConnection()
    connection.connect()
    #connection.seed("./seeds/users.sql")
    #Below more appropriate than seeding since it is just one command required
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('testuser', 'password123');")

   # send the request
    response = client.post('/sessions', data={
        'username': 'testuser',
        'password': 'password1234'
    })

    # assert that the redirect happened, note that redirects in flask only support 3xx by default, 401 will go to 401 page
    assert response.status_code == 302

    # assert that user is returned to login page
    assert response.headers['Location'].endswith('/sessions/new')
