from user import User

class UserRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all books
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        books = []
        for row in rows:
            item = User(row["username"], row["password"], row["id"])
            books.append(item)
        return books

    def find(self, username):
        rows = self._connection.execute(
            'SELECT * from users WHERE username = %s', [username])
        if rows:
            row = rows[0]
            return User(row["username"], row["password"], row["id"])
        else:
            return None

    def create(self, user):
        self._connection.execute('INSERT INTO users (username, password) VALUES (%s, %s)', [
                                 user.username, user.password])
        return None

    # Delete an book by their id
    def delete(self, user_id):
        self._connection.execute(
            'DELETE FROM users WHERE id = %s', [user_id])
        return None