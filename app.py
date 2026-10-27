from flask import Flask, render_template # Add 'render_template' to your listed imports from Flask
from database_connection import DatabaseConnection
from book_repository import BookRepository

# instantiate a Flask app object
app = Flask(__name__)

# Declares a route that listens for a GET request to the path /hello
# and a method to execute when that request comes in
@app.route('/hello', methods=['GET'])
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


# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

