from flask import Flask, render_template, request, url_for
from flask_mail import Mail, Message
import sqlite3
import os
from os import path

import websiteconfig

# from dotenv import load_dotenv



app = Flask(__name__)


# app.config.from_pyfile('/home/lainofthewired/survey/config_file.cfg')
app.config.from_pyfile('/home/lainofthewired/config_file.cfg')


# project_folder = os.path.expanduser('/Users/mandywoo/Documents/survey_project')
# load_dotenv(os.path.join(project_folder, '.env'))

# custom_email = os.environ.get('custom_email')
# email_password = os.environ.get('email_password')
# my_email = os.environ.get('my_email')
custom_email = websiteconfig.custom_email
email_password = websiteconfig.email_password
my_email = websiteconfig.my_email

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = custom_email
app.config['MAIL_PASSWORD'] = email_password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def password():
    return render_template('password.html')

@app.route('/surveyf')
def survey_1_entry():
    return render_template('survey_1.html')

@app.route('/surveygf')
def survey_2_entry():
    return render_template('survey_2.html')


@app.route('/addsurvey_1', methods = ['POST', 'GET'])
def add_data_1():
    if request.method == 'POST':
        try:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            phone_number = request.form['phone_number']
            question_1 = request.form['question_1']
            question_2 = request.form['question_2']
            question_3 = request.form['question_3']
            question_4 = request.form['question_4']
            question_5 = request.form['question_5']
            question_6 = request.form['question_6']
            question_7 = request.form['question_7']
            question_8_r1 = request.form['question_8_r1']
            question_8_r2 = request.form['question_8_r2']
            question_8_r3 = request.form['question_8_r3']
            question_8_r4 = request.form['question_8_r4']
            question_9 = ' '.join(request.form['question_9'].split('T'))
            question_10 = request.form['question_10']

            with sqlite3.connect("/home/lainofthewired/survey/database.db") as con:
            # with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO survey_1 (first_name, last_name, email, phone_number, question_1,\
                    question_2, question_3, question_4, question_5, question_6, question_7, question_8_r1,\
                    question_8_r2, question_8_r3, question_8_r4, question_9, question_10) VALUES (?, ?, ?,\
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (first_name, last_name, email, phone_number, question_1,\
                    question_2, question_3, question_4, question_5, question_6, question_7, question_8_r1,\
                    question_8_r2, question_8_r3, question_8_r4, question_9, question_10))
                con.commit()
                msg = "Record successfully added"
        except Exception as e:
            con.rollback()
            msg = 'error in insert operation, error:' + str(e)
        else:
            # con = sqlite3.connect('database.db')
            con = sqlite3.connect("/home/lainofthewired/survey/database.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute('SELECT * FROM survey_1 ORDER BY id DESC LIMIT 1')
            row = cur.fetchone()
            try:
                print(custom_email)
                send_mail('Frenship Survey Response', custom_email, [row[3]],
                            render_template('survey_1_email.html', row=row))
                send_mail('Frenship Survey Response', custom_email, [my_email],
                            render_template('my_survey_1_email.html', row=row))
            except Exception as e:
                print('error in email: ' + str(e))
        finally:
            con.close()
            return render_template('closing.html')

@app.route('/addsurvey_2', methods = ['POST', 'GET'])
def add_data_2():
    if request.method == 'POST':
        try:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            phone_number = request.form['phone_number']
            question_1 = request.form['question_1']
            question_2 = request.form['question_2']
            question_3 = request.form['question_3']
            question_4 = request.form['question_4']
            question_5 = request.form['question_5']
            question_6 = request.form['question_6']
            question_7 = request.form['question_7']
            question_8_r1 = request.form['question_8_r1']
            question_8_r2 = request.form['question_8_r2']
            question_8_r3 = request.form['question_8_r3']
            question_8_r4 = request.form['question_8_r4']
            question_8_r5 = request.form['question_8_r5']
            question_9 = ' '.join(request.form['question_9'].split('T'))
            question_10 = request.form['question_10']

            with sqlite3.connect("/home/lainofthewired/survey/database.db") as con:
            # with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO survey_2 (first_name, last_name, email, phone_number, question_1,\
                    question_2, question_3, question_4, question_5, question_6, question_7, question_8_r1,\
                    question_8_r2, question_8_r3, question_8_r4, question_8_r5, question_9, question_10) VALUES (?, ?, ?,\
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (first_name, last_name, email, phone_number, question_1,\
                    question_2, question_3, question_4, question_5, question_6, question_7, question_8_r1,\
                    question_8_r2, question_8_r3, question_8_r4, question_8_r5, question_9, question_10))
                con.commit()
                msg = "Record successfully added"
        except Exception as e:
            con.rollback()
            msg = 'error in insert operation, error:' + str(e)
        else:
            # con = sqlite3.connect('database.db')
            con = sqlite3.connect("/home/lainofthewired/survey/database.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute('SELECT * FROM survey_2 ORDER BY id DESC LIMIT 1')
            row = cur.fetchone()
            send_mail('Relationship Survey Response', custom_email, [row[3]],
                        render_template('survey_2_email.html', row=row))
            send_mail('Relationship Survey Response', custom_email, [my_email],
                        render_template('my_survey_2_email.html', row=row))
        finally:
            con.close()
            return render_template('closing.html')


@app.route('/survey_list')
def list1():
    con = sqlite3.connect("/home/lainofthewired/survey/database.db")
    # con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM survey_1')
    rows = cur.fetchall()
    return render_template('list_1.html', rows=rows)

@app.route('/survey_lis')
def list2():
    con = sqlite3.connect("/home/lainofthewired/survey/database.db")
    # con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM survey_2')
    rows = cur.fetchall()
    return render_template('list_2.html', rows=rows)

@app.route('/questions_list_f')
def q_list_1():
    ROOT = path.dirname(path.realpath(__file__))
    # con = sqlite3.connect(path.join(ROOT, "database.db"))
    con = sqlite3.connect("/home/lainofthewired/survey/database.db")
    # con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM questions_list_f')
    row = cur.fetchone()
    return render_template('questions_list_1.html', row=row)

@app.route('/questions_list_gf')
def q_list_2():
    ROOT = path.dirname(path.realpath(__file__))
    # con = sqlite3.connect(path.join(ROOT, "database.db"))
    con = sqlite3.connect("/home/lainofthewired/survey/database.db")
    # con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM questions_list_gf')
    row = cur.fetchone()
    return render_template('questions_list_2.html', row=row)


def send_mail(header, sender, recipients, html):
    msg = Message(header, sender = sender, recipients=recipients)
    msg.body = "Thank you for taking part in the survey."
    msg.html = html
    mail.send(msg)


if __name__ == '__main__':
    app.run(debug=True)
