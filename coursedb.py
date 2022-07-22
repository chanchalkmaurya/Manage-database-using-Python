import sqlite3 as lite


class ManageDatabase(object):

    def __init__(self):
        global con 
        try:
            con = lite.connect("courses.db")

            with con:
                cur = con.cursor()
                sql = "CREATE TABLE IF NOT EXISTS course(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,\
                    description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)"
                cur.execute(sql)
        except Exception:
            print("Unable to connect to database")

    # TODO: insert data into database
    def insert_data(self, data):
        try:
            cur = con.cursor()
            sql = "INSERT INTO course (name, description, price, is_private) \
                VALUES (?, ?, ?, ?)"
            cur.execute(sql, data)
            return True
        except Exception:
            return False


    # TODO: fetch data from database
    def fetch_data(self):
        try:
            cur = con.cursor()
            sql = "SELECT * FROM course"
            cur.execute(sql)
            return cur.fetchall()

        except Exception:
            return False


    # TODO: delete the data from the database
    def delete_data(self, id):
        try:
            cur = con.cursor()
            sql = "DELETE FROM course WHERE id = ?"
            cur.execute(sql, [id])
            return True
        except Exception:
            return False



