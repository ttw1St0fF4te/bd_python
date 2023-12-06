import sqlite3

class EmployeesDB:
    def __init__(self, db_name='photocenter.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                full_name TEXT,
                email TEXT,
                phone_number TEXT,
                FOREIGN KEY (user_id) REFERENCES Users(id)
            )
        ''')
        self.conn.commit()

    def register_employee(self, username, full_name, email, phone_number):
        user = self.cursor.execute('SELECT id FROM Users WHERE username=?', (username,)).fetchone()
        user_id = user[0]

        self.cursor.execute('INSERT INTO Employees (user_id, full_name, email, phone_number) VALUES (?, ?, ?, ?)',
                            (user_id, full_name, email, phone_number))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
