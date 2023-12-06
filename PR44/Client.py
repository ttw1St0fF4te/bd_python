import sqlite3

class ClientsDB:
    def __init__(self, db_name='photocenter.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                full_name TEXT,
                email TEXT,
                phone_number TEXT,
                product_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES Users(id),
                FOREIGN KEY (product_id) REFERENCES Products(id)
            )
        ''')
        self.conn.commit()

    def register_client(self, username, full_name, email, phone_number, product_id=None):
        user = self.cursor.execute('SELECT id FROM Users WHERE username=?', (username,)).fetchone()
        user_id = user[0]
     

        self.cursor.execute('INSERT INTO Clients (user_id, full_name, email, phone_number, product_id) VALUES (?, ?, ?, ?, ?)',
                            (user_id, full_name, email, phone_number, product_id))
        self.conn.commit()

    def get_client_orders(self, user_id):
        self.cursor.execute('''
            SELECT Products.name, Products.price
            FROM Clients
            JOIN Products ON Clients.product_id = Products.id
            WHERE Clients.user_id = ?
        ''', (user_id,))
        return self.cursor.fetchall()

    def update_client_profile(self, user_id, full_name, email, phone_number):
        self.cursor.execute('''
            UPDATE Clients
            SET full_name=?, email=?, phone_number=?
            WHERE user_id=?
        ''', (full_name, email, phone_number, user_id))
        self.conn.commit()

    def add_order_to_client(self, user_id, product_id):
        self.cursor.execute('UPDATE Clients SET product_id=? WHERE user_id=?', (product_id, user_id))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
