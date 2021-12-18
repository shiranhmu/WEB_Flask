from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__)

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
    print('I am in about')
    return render_template('assignment8.html',
     profile={'Name': 'Shiran','Second_Name':'Hamou'},
     university='Bgu',
     hobbies=('sport','music','trips', 'sql', 'fun'))

if __name__ == '__main__':
    app.run(debug=True)