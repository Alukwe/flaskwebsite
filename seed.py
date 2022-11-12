import sqlite3

connection = sqlite3.connect('data.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute(
    '''INSERT INTO userinfor(
            fname,
            lname,
            number,
            email ,
            password1 ,
            password2
            )VALUES(
            'Jones',
            'Alukwe',
            '0745983042',
            'terahjones@gmail.com',
            'alukwetj3.',
            'alukwetj3.'
    );'''

)

cursor.execute(
    '''INSERT INTO userinfor(
            fname,
            lname,
            number,
            email ,
            password1 ,
            password2
            )VALUES(
            'Jane',
            'Willfree',
            '0733980289',
            'tj.papajones@gmail.com',
            'Alukwetj3.',
            'Alukwetj3.'
    );'''

)
connection.commit()
cursor.close()
connection.close()

connection = sqlite3.connect('data.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute(
    '''INSERT INTO Messages(
            name,
            email ,
            message 
            )VALUES(
            'Jones Alukwe',
            'terahjones3@gmail.com',
            'Testing 123'
    );'''

)

cursor.execute(
    '''INSERT INTO Messages(
            name,
            email ,
            message 
            )VALUES(
            'Jane Willfree',
            'tj.papajones@gmail.com',
            'Does this really work ??'
    );'''

)
connection.commit()
cursor.close()
connection.close()
