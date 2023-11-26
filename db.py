import sqlite3


def is_number(_str):
    try:
        int(_str)
        return True
    except ValueError:
        return False

class Database:
    def __init__(self, db_file):
        self.connect = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connect.cursor()

    def get_keyboard(self):
        with self.connect:
            return self.cursor.execute('SELECT * FROM rules').fetchall()


    def check_db(self):
        with self.connect:
            return self.cursor.execute('SELECT * FROM rules').fetchall()

    def get_keyboard_name(self, id_or_name):
        with self.connect:
            if is_number(id_or_name):
                return self.cursor.execute('SELECT * FROM rules WHERE id=?', (id_or_name, )).fetchone()
            else:
                return self.cursor.execute('SELECT * FROM rules WHERE keyboard_name=?', (id_or_name,)).fetchone()

    def get_callback_data(self, id_or_name):
        with self.connect:
            if is_number(id_or_name):
                return self.cursor.execute('SELECT * FROM rules WHERE id=?', (id_or_name,)).fetchone()
            else:
                return self.cursor.execute('SELECT * FROM rules WHERE callback_data=?', (id_or_name,)).fetchone()

    def get_rules(self, id_or_name):
        with self.connect:
            if is_number(id_or_name):
                return self.cursor.execute('SELECT * FROM rules WHERE id=?', (id_or_name,)).fetchone()
            else:
                return self.cursor.execute('SELECT * FROM rules WHERE rules=?', (id_or_name,)).fetchone()

    def get_callback_data_all(self):
        with self.connect:
            return self.cursor.execute('SELECT * FROM rules').fetchall()


    def insert_rule(self, btn_name, callback_data, rules):
        with self.connect:
            return self.cursor.execute('INSERT INTO rules(keyboard_name, callback_data, rules) VALUES(?, ?, ?)', (f"{btn_name}", f"{callback_data}", f"{rules}", ))

    def delete_rules(self, btn_name):
        with self.connect:
            return self.cursor.execute('DELETE FROM rules WHERE keyboard_name=?', (f"{btn_name}", ))
