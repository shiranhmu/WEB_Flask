from flask import Flask, redirect, url_for
from flask import render_template, request, session

app = Flask(__name__)
app.secret_key = '123'

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
    if 'user_inside' in session:
        if session['user_inside']:
            print('user_inside')
    if 'product' in request.args:
        product= request.args['product']
        size= request.args['size']
        return render_template('catalog.html', p_name=product, p_size=size)
    return render_template('catalog.html')


#assignment9
Users = [{"user": "Yossi", "email": "yo@gmail.com"},
         {"user": "Shiran", "email": "sh@gmail.com"},
         {"user": 'Dotan', "email": "do@gmail.com"},
         {"user": "Linor", "email": "li@gmail.com"},
        {"user": "Oz", "email": "oz@gmail.com"}]

@app.route('/logout')
def logout_func():
    session['UserName']= ''
    return render_template('cv1.html')


@app.route('/assignment9', methods=['GET', 'POST'])
def login_func():
    if request.method == 'GET':
        if 'searchinput' in request.args:
            search = request.args['searchinput']
        else:
            search = ""
        if search == "": #empty string
            return render_template('assignment9.html' , search=Users)
        flag = False
        for user in Users:
            if user['user'] == search or user['email'] == search:
                flag = True
                return render_template('assignment9.html', searchfound=user)
        if not flag:
            return render_template('assignment9.html', notfound="not found!")

    # GET ->args  POST -> form
    if request.method == 'POST':
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



if __name__ == '__main__':
    app.run(debug=True)