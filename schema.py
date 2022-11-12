import sqlite3

connection = sqlite3.connect('data.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute(
    '''CREATE TABLE userinfor(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            fname varchar(16),
            lname varchar(16),
            number integer,
            email varchar(16),
            password1 varchar(32),
            password2 varchar(32)
    );'''

)
connection.commit()
cursor.close()
connection.close()


connection = sqlite3.connect('data.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute(
    '''CREATE TABLE Messages (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            name varchar(30),
            email varchar(30),
            message varchar(1000)
    );'''

)
connection.commit()
cursor.close()
connection.close()