from flask import Flask

# instantiate a Flask app object
app = Flask(__name__)

# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(port=5001, debug=True)
