# import time

from functools import wraps

# import mail
from flask import *
from flask_wtf import FlaskForm
from jinja2 import TemplateNotFound
from wtforms import StringField, SubmitField, TextAreaField, validators

import models

# from past.builtins import raw_input
# from selenium.webdriver.chrome import webdriver

app = Flask(__name__)
app.secret_key = 'AlukweJones'
email = ''
use = models.check_users()


class ContactForm(FlaskForm):
    name = StringField('Full Name', [validators.DataRequired("Please enter your name")])
    email = StringField('Email', [validators.DataRequired("Please enter your email address"),
                                  validators.Email("Please enter your email address")])
    message = TextAreaField('Type your message here...', [validators.DataRequired("Please enter you message")])
    submit = SubmitField("Send")


# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_SERVER"] = 465
# app.config["MAIL_SERVER"] = True
# app.config["MAIL_SERVER"] = 'tj.papajones@gmail.com'
# app.config["MAIL_SERVER"] = 'alukwetj3.'
#
# mail.init_app(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    # set the 404 status explicitl


@app.errorhandler(505)
def page_not_found(e):
    return render_template('505.html'), 505


@app.route('/', methods=['GET'])
def home():
    try:
        if 'email' in session:
            g.user = session['email']
            return render_template('DashBoard.html')

        return render_template('home.html')
    except TemplateNotFound:
        return redirect('404.html'), 404


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            session.pop('email', None)
            areyouuser = request.form['email']
            pwd = models.check_pw(areyouuser)
            if request.form['email'] == '' and request.form['password'] == '':
                return render_template('login.html', message='Unfilled Fields')
            elif request.form['email'] == '':
                return render_template('login.html', message='email required')
            elif request.form['password'] == '':
                return render_template('login.html', message='password required')
            elif request.form['password'] != pwd:
                return render_template('login.html', message='Invalid password or user !')

            else:
                if request.form['password'] == pwd:
                    session['email'] = request.form['email']
                    return redirect(url_for('DashBoard'))
        return render_template('login.html', message='Please Login')
    except 404:
        return redirect('404.html'), 404


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    try:
        if request.method == 'GET':
            message = 'Please Sign Up'
            return render_template('signup.html', message=message)
        else:
            fname = str(request.form['fname'].upper().lower())
            lname = str(request.form['lname'].upper().lower())
            number = request.form['number']

            email = request.form['email']

            password1 = request.form['password1']
            password2 = request.form['password2']

            message = models.signup(fname, lname, number, email, password1, password2)
            return message
    except RuntimeError:
        return render_template('signup.html', message="Something went wrong ")


#     render_template('football.html', message=message)

def login_requried(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('email') is None or session.get('if_logged') is None:
            return redirect('/login', code=302)
        return f(*args, **kwargs)

    return decorated_function


@app.route('/DashBoard', methods=['GET'])
@login_requried
def DashBoard():
    return render_template('DashBoard.html')


@app.before_request
def before_request():
    g.email = None
    if 'email' in session:
        g.email = session['email']


@app.route('/getsession')
def getsession():
    if 'email' in session:
        return session['email']
    return redirect(url_for('login'))


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    cform = ContactForm()
    if request.method == 'POST':
        if cform.validate_on_submit() == False:
            flash("All fields are required")
            return render_template('contact.html', form=cform)
        else:
            flash('Your message was received successfully.Your feedback will be relayed shortly', category='success')
        return render_template('contact.html', form=cform)
    return render_template('contact.html', form=cform)


@app.route('/comingsoon', methods=['GET'])
def comingsoon():
    return render_template('comingsoon.html')


@app.route('/service', methods=['GET'])
def service():
    return render_template('service.html')


@app.route('/web_dev_img', methods=['GET'])
def web_dev_img():
    return render_template('web_dev_img.html')


@app.route('/sys_app_img', methods=['GET'])
def sys_app_img():
    return render_template('sys_app_img.html')


@app.route('/soft_drive_install_img', methods=['GET'])
def soft_drive_install_img():
    return render_template('soft_drive_install_img.html')


@app.route('/repair_diagnose_img', methods=['GET'])
def repair_diagnose_img():
    return render_template('repair_diagnose_img.html')


@app.route('/mrkt_biz_ad_img', methods=['GET'])
def mrkt_biz_ad_img():
    return render_template('mrkt_biz_ad_img.html')


@app.route('/learn', methods=['GET'])
def learn():
    return render_template('learn.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('About.html')


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('home'))


@app.route('/backhome')
def backhome():
    session.pop('email', None)
    return redirect(url_for('home'))


#
# x = raw_input("http://127.0.0.1:7000")
# refreshrate = raw_input("3")
# refreshrate = int(refreshrate)
# driver = webdriver.Firefox()
# driver.get('http://' + x)
# while True:
#     time.sleep(refreshrate)
#     driver.refresh()

if __name__ == '__main__':
    while True:
        app.run(host='0.0.0.0', port=7000, debug=True)
