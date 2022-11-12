import re
import sqlite3
from sqlite3 import OperationalError

from flask import *


# checking the color that the user likes and selecting it

def check_number(email):
    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        '''SELECT number FROM userinfor WHERE email='{email}'ORDER BY pK DESC

        ;'''.format(email=email))
    num1 = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    message = '{email} number is {num1}'.format(email=email, num1=num1)
    return message


# user password validation


def check_pw(email):
    try:
        connection = sqlite3.connect('data.db', check_same_thread=False)
        cursor = connection.cursor()
        cursor.execute(
            '''SELECT password1, password2 FROM userinfor WHERE email='{email}'ORDER BY pK DESC

           ;'''.format(email=email))
        password = cursor.fetchone()[0]

        connection.commit()
        cursor.close()
        connection.close()
        return password
    except TypeError:
        print(TypeError)
        return render_template('signup.html', message='An error occurred')


def signup(fname, lname, number, email, password1, password2):
    try:
        connection = sqlite3.connect('data.db', check_same_thread=False)
        cursor = connection.cursor()
        # runs to check if there is any user
        cursor.execute(
            '''SELECT password1, password2 FROM userinfor WHERE email = '{email}'

         ;'''.format(email=email))
        # if the does not exit it will return an empty list
        exist = cursor.fetchone()

        if exist is None:
            cursor.execute(
                '''INSERT INTO userinfor(
                     fname,
                     lname,
                     number,
                     email ,
                     password1 ,
                     password2 
                     )VALUES(
                     '{fname}',
                     '{lname}',
                     '{number}',
                     '{email}',
                     '{password1}',
                     '{password2}'
             );'''.format(fname=fname.upper().lower(), lname=lname.upper().lower(), number=number,
                          email=email,
                          password1=generate_password_hash(password1, method='sha256'),
                          password2=generate_password_hash(password2, method='sha256')))

            # allowed_domains = "kabarak.ac.ke, gmail.com, yahoo.com, icloud.com, hotmail.com"
            space = ' '
            numeric = ''' 0123456789<>?'|":{},./\;[]+_=-()*;&^%$#@!~  '''
            # '''Email patterns (regex_1 and regex)'''
            # regex_1 = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
            regex = '^[a-zA-Z0-9-_]+[\._]?[a-zA-Z0-9]+[a-zA-Z]+\d[@]\w+[.][a-z]{2,3}$'
            # "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            # name pattern
            alphabet = "^\A[a-z]+.[a-zA-Z]+\S.$"
            if fname == '' or lname == ' ' or number == '' or email == '' or password1 == '' or password2 == '':
                flash("Unfilled Field(s)", category="error")
                return render_template('signup.html', message='Unfilled Field(s) !')
            elif not re.search(alphabet, fname):
                return render_template('signup.html', message='Invalid first name!')
            elif not re.search(alphabet, lname):
                return render_template('signup.html', message='Invalid last name!')
            elif len(fname) < 2 or len(lname) < 2:
                return render_template('signup.html', message='Invalid name(s) ! Too short !')
            elif len(fname) > 16 or len(lname) > 16:
                return render_template('signup.html', message='Invalid name(s) !Too long !')
            elif len(number) != 10:
                return render_template('signup.html', message='Invalid phone number ! too short/too long')
            elif not re.search(regex, email):
                return render_template('signup.html', message='Invalid email!')
            elif len(email) < 5:
                return render_template('signup.html', message='Email is too short !')
            elif len(email) > 50:
                return render_template('signup.html', message='Email is too long !')
            elif len(password1) < 8:
                return render_template('signup.html', message='Password is too short ! ')
            elif len(password1) > 16:
                return render_template('signup.html', message='Password is too long! You might  forget ')
            elif password2 != password1:
                return render_template('signup.html', message='Passwords do not match ! ')
            elif True:
                try:
                    for num in fname:
                        if num in numeric:
                            return render_template('signup.html',
                                                   message='Name must only contain characters !')
                    for white_space in fname:
                        if white_space in space:
                            return render_template('signup.html', message='White space are not allowed ! ')
                    for num in lname:
                        if num in numeric:
                            return render_template('signup.html',
                                                   message='Your last name must only contain characters ! ')
                    for white_space in lname:
                        if white_space in space:
                            return render_template('signup.html', message='White space are not allowed ! ')
                    for char in number:
                        if char in alphabet:
                            return render_template('signup.html', message='Invalid number ! ')
                    for white_space in number:
                        if white_space in space:
                            return render_template('signup.html', message='White space are not allowed ! ')
                    for white_space in password1:
                        if white_space in space:
                            return render_template('signup.html', message='White space are not allowed ! ')
                    for white_space in password2:
                        if white_space in space:
                            return render_template('signup.html', message='White space are not allowed ! ')
                except OperationalError:
                    return render_template('signup.html', message='AN error occurred !')

            connection.commit()
            cursor.close()
            connection.close()
        elif fname == '' or lname == ' ' or number == '' or email == '' or password1 == '' or password2 == '':
            return render_template('signup.html', message='Unfilled Field(s) ')

        else:
            return render_template('signup.html', message='User Already Exists')

        return redirect(url_for('DashBoard'))
    except RuntimeError:

        render_template('signup.html')


def check_users():
    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        '''SELECT email FROM INFORM ORDER BY pK DESC

        ;''')
    db_users = cursor.fetchall()
    users = []
    for i in range(len(db_users)):
        person = db_users[i][0]
        users.append(person)

    connection.commit()
    cursor.close()
    connection.close()


def contact(name, email, message):
    connection = sqlite3.connect('data.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        '''SELECT email  FROM userinfor WHERE email = '{email}'

        ;'''.format(email=email))

    Email = cursor.fetchone()[0]
    if Email is None:
        cursor.execute(
            '''INSERT INTO Message(
                 name,
                 email,
                 message 
                 )VALUES(
                 '{name}',
                 '{email}',
                 '{message}'
         );'''.format(name=name, email=generate_email_hash(email, method='sha256'), message=message))
        numeric = ''' 0123456789<>?'|":{},./\;[]+_=-()*;&^%$#@!~  '''
        regex = '^[a-zA-Z0-9-_]+[\._]?[a-zA-Z0-9]+[a-zA-Z]+\d[@]\w+[.][a-z]{2,3}$'
        alphabet = "^\A[a-z]+.[a-zA-Z]+\S.$"
        if name == '' and email == '' and message == '':
            return render_template('signup.html', message='Unfilled Field(s) !')
        elif name == '':
            return render_template('signup.html', message='Unfilled Field for name  !')
        elif not re.search(alphabet, name):
            return render_template('signup.html', message='Invalid first name!')
        elif not re.search(regex, email):
            return render_template('signup.html', message='Invalid email!')
        elif len(email) < 5:
            return render_template('signup.html', message='Email is too short !')
        elif len(email) > 50:
            return render_template('signup.html', message='Email is too long !')
        elif True:
            for num in fname:
                if num in numeric:
                    return render_template('contact.html', message='Name must only contain characters !')

        connection.commit()
        cursor.close()
        connection.close()
    elif name == '' or email == '' or message == '':
        return render_template('contact.html', message='Unfilled Field(s) ')

    else:

        return render_template('contact.html', message='User Already Exists')

    return render_template('contact.html', message='')

    render_template('contact.html')
