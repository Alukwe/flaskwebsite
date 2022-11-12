import sqlite3

connection = sqlite3.connect('data.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute(
    '''DELETE  FROM userinfor ;'''


)
connection.commit()
cursor.close()
connection.close()
connection = sqlite3.connect('data.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute(
    '''DELETE  FROM Messages ;'''

)
connection.commit()
cursor.close()
connection.close()