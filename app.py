from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/home_page')
@app.route('/home')
@app.route('/')
def hello_func():
    return 'Welcome to Hello Page :) !'

#one usage of redirect() and url_for() functions
@app.route('/about')
def about_func():
    print('I am in about')
    return redirect(url_for('catalog_func'))

@app.route('/catalog')
def catalog_func():
    return 'Welcome to Catalog Page!'

#one usage of redirect() function
@app.route('/feed')
def feed_func():
    print('I am in feed')
    return redirect('/home')


if __name__ == '__main__':
    app.run(debug=True)

