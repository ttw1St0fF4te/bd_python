import sqlite3

class AdminDB:
    def __init__(self, db_name='photocenter.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def check_admin_password(self, password):
        # Предположим, что администраторский пароль - "admin_password"
        return password == "admin_password"

    def delete_user(self, user_id):
        self.cursor.execute('DELETE FROM Users WHERE id=?', (user_id,))
        self.conn.commit()

    def update_user(self, user_id, username, password, role):
        self.cursor.execute('''
            UPDATE Users
            SET username=?, password=?, role=?
            WHERE id=?
        ''', (username, password, role, user_id))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()