import sqlite3

class UsersDB:
    def __init__(self, db_name='photocenter.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT,
                role TEXT
            )
        ''')
        self.conn.commit()

    def register_user(self, username, password, role):
        self.cursor.execute('INSERT INTO Users (username, password, role) VALUES (?, ?, ?)', (username, password, role))
        self.conn.commit()

    def login_user(self, username, password):
        self.cursor.execute('SELECT * FROM Users WHERE username=? AND password=?', (username, password))
        return self.cursor.fetchone()

    def close_connection(self):
        self.conn.close()