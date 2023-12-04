import sqlite3

class ProductsDB:
    def __init__(self, db_name='photocenter.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price REAL
            )
        ''')
        self.conn.commit()

    def get_all_products(self):
        self.cursor.execute('SELECT * FROM Products')
        return self.cursor.fetchall()

    def add_product(self, name, price):
        self.cursor.execute('INSERT INTO Products (name, price) VALUES (?, ?)', (name, price))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()