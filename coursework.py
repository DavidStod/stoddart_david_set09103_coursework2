from flask import Flask, render_template, url_for, redirect, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)


app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello David! <a href='/logout/'>Logout</a>"

@app.route('/login/', methods=['POST'])
def do_admin_login():

    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flask('wrong password!')
    return home()

@app.route('/logout/')
def logout():
    session['logged_in'] = False
    return home()

#open every page by reading it from the url
#@app.route('/<name>/', methods=['GET', 'POST'])
#def guitar(name=None):
#    return render_template('{0}.html'.format(name), name=name), 200

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', debug=True)
