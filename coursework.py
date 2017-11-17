from flask import Flask
from flask import Flask, flash, render_template, url_for, redirect, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/log/', methods=['GET', 'POST'])
def login():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return home()

@app.route('/basket/', methods=['GET', 'POST'])
def basket():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('basket.html')
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
        print('wrong password')
    return login()

@app.route('/logout/')
def logout():
    session['logged_in'] = False
    return login()

@app.route('/get_the_order/')
def get_the_order():
    global the_order_list

    the_order_list = []
    sun_list = []

    get_order = request.args.get('menu_order', 0, type=str)
    get_price = request.args.get('price_order', 0, type=str)

    the_order_list.append(get_order)
    sum_list.append(get_price)

    session['theOrder'] = ' '.join(the_order_list)
    session['price'] = ' '.join(sum_list)

    return jsonify(result=the_order_list + sum_list)

#open every page by reading it from the url
@app.route('/guitar/<name>/', methods=['GET', 'POST'])
def guitar(name=None):
    return render_template('{0}.html'.format(name), name=name), 200

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', debug=True)
