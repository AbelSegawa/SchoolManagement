from database.db import get_conn

class Student:
    @staticmethod
    def add(name, grade):
        conn = get_conn()
        conn.execute('INSERT INTO students (name, grade) VALUES (?,?)', (name, grade))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_conn()
        data = conn.execute('SELECT * FROM students').fetchall()
        conn.close()
        return data
