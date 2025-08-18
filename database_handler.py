import sqlite3
import database_handler

class DatabaseHandler:
    DB_NAME='student.db'


    @staticmethod
    def _connect():        #this makes it private
        return sqlite3.connect(DatabaseHandler.DB_NAME)
    
    @staticmethod
    def create_table():
        with DatabaseHandler._connect() as conn:
            conn.execute('''CREATE TABLE IF NOT EXIST students
                        ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        gender TEXT NOT NULL )''')
        
    @staticmethod
    def insert_student(name ,email,age,gender):
        with DatabaseHandler._connect() as conn:
            conn.execute("INSERT INTO students (name,email,age,gender) VALUES (?,?,?,?)",(name ,email,age,gender))

    @staticmethod
    def get_all__students():
        with DatabaseHandler._connect() as conn:
            cursor=conn.execute("SELECT * FROM students")
            students=cursor.fetchall()
            return students


DatabaseHandler.create_table()

  
