from flask import Flask, request, redirect, render_template, session, abort # Add 'render_template' to your listed imports from Flask
from flask_bcrypt import Bcrypt
from database_connection import DatabaseConnection
from book_repository import BookRepository
from book import Book
from user_repository import UserRepository
from user import User
from login_required import login_required

# instantiate a Flask app object
app = Flask(__name__)
app.secret_key = "some_really_secret_key"
bcrypt = Bcrypt(app)


# Declares a route that listens for a GET request to the path /hello
# and a method to execute when that request comes in
@app.route('/hello', methods=['GET'])
@login_required
def hello():
    return "Hello to you too"

@app.route('/books', methods=['GET'])
def books():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    books = book_repository.all()
    print(books)
    return render_template("books.html", books=books)

@app.route('/books', methods=['POST'])
@login_required
def create_book():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)

    book_details = request.form
    book = Book(book_details["title"], book_details["author"])
    
    book_repository.create(book)
    return redirect("/books")

@app.route('/authors', methods=['GET'])
def authors():
    return [
  {
    "name": "Julia Donaldson",
    "dob": "1948-09-16"
  },
  {
    "name": "Andrea Beaty",
    "dob": "1961-10-08"
  },
  {
    "name": "Kelly Barnhill",
    "dob": "1973-01-01"
  },
  {
    "name": "Zetta Elliott",
    "dob": "1979-11-11"
  }
]

@app.route('/team', methods=['GET'])
def get_team():
    team = ["Dorothy", "Rose", "Blanche", "Sophia"]
    return render_template("team.html", team=team)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/users/new", methods=["GET"])
def get_registration_page():
    return render_template("signup_form.html")

@app.route('/users', methods=['POST'])
def create_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)

    user_details = request.form
    hashed_password = bcrypt.generate_password_hash(user_details["password"]).decode('utf-8')
    user = User(user_details["username"], hashed_password)
    
    user_repository.create(user)
    return redirect("/")

@app.route('/sessions/new', methods=['GET'])
def get_login_page():
    return render_template("login_form.html")

@app.route('/sessions', methods=['POST'])
def create_session():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)

    username = request.form["username"]
    password = request.form["password"]

    user = user_repository.find(username)
    print(bcrypt.check_password_hash(user.password, password))
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    print(user.password, hashed_password)

    if user and bcrypt.check_password_hash(user.password, password):
        session['username'] = username
        session['uid'] = user.id
        return redirect("/books")
    else:
        return redirect("/sessions/new")


# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

