from flask import Flask, redirect, url_for, Blueprint
from flask import render_template, request, session
from flask import json, jsonify
import requests
import os, sys

from interact_with_DB import interact_db


app = Flask(__name__)
app.secret_key = '123'
app.config.from_pyfile('settings.py')

#assignment8
@app.route('/home_page')
@app.route('/home')
@app.route('/')
def hello_func():
    #DB
    found = True
    if found:
        return render_template('cv1.html', username='Shiran')
    else:
        return render_template('cv1.html')

@app.route('/contact')
def contact_func():
    return render_template('contact.html')

@app.route('/myCV' )
def myCV_func():
    return  render_template('cv2.html')

@app.route('/assignment8')
def about_func():
    return render_template('assignment8.html',
                    profile={'Name': 'Shiran','Second_Name':'Hamou'},
                    university='Bgu',
                    hobbies=('sport','music','trips', 'sql', 'fun'))

@app.route('/catalog')
def catalog_func():
    if 'UserName' in session:
        if session['UserName']:
            print('UserName')
    if 'product' in request.args:
        product= request.args['product']
        size= request.args['size']
        return render_template('catalog.html', p_name=product, p_size=size)
    return render_template('catalog.html')


#assignment9
Users = {"user1": {"User": "Yossi", "Email": "yo@gmail.com"},
         "user2": {"User": "Shiran", "Email": "sh@gmail.com"},
         "user3": {"User": "Dotan", "Email": "do@gmail.com"},
         "user4": {"User": "Linor", "Email": "li@gmail.com"},
         "user5": {"User": "Oz", "Email": "oz@gmail.com"} }

@app.route('/logout')
def logout_func():
    session['UserName']= ''
    return render_template('cv1.html')


@app.route('/assignment9', methods=['GET', 'POST'])
def login_func():
    if request.method == 'GET':
        if 'searchinput' in request.args:
            search = request.args['searchinput']
            return render_template('assignment9.html', UserName=session['UserName']
                                                     , search=search
                                                     , Users=Users)
        return render_template('assignment9.html', Users=Users)

    # GET ->args  POST -> form
    elif request.method == 'POST':
        UserName = request.form['UserName']
        Password = request.form['Password']
        #DB
        found = True
        if found:
            session['UserName']= UserName
            session['user_inside']= True
            return render_template('assignment9.html', UserName=UserName, Users=Users)
        else:
            return render_template('assignment9.html')

## assignment10
from assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

# assignment11
@app.route('/assignment11', methods=['GET'])
def assignment11_func():
    return render_template('assignment11.html')

def get_usersFromLink(num):
    res = requests.get(f'https://reqres.in/api/users/{num}')
    res = res.json()
    return res


@app.route('/assignment11/users' )
def users_MyDB_func():#return a list of users from a table ‘users’ from myDB in json format
    myDB = {}
    query = "select * from users ;"
    query_result = interact_db(query=query, query_type='fetch')
    for user in query_result:
        myDB[f'{user.id}'] = {'id': user.id, 'name': user.name,
                              'email': user.email, 'password': user.password }
    return render_template('assignment11.html', query_result=myDB)

@app.route('/assignment11/outer_source')
def users_outSource_func():
    num = 1
    if "backend" in request.args: #backend form
        num = int(request.args['backend'])
        user = get_usersFromLink(num)
        return render_template('assignment11.html', backend=user)
    else:
        return render_template('assignment11.html')

if __name__ == '__main__':
    app.run(debug=True)
