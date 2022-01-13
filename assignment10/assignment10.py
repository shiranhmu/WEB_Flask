from flask import Blueprint, redirect
from flask import render_template, request
from interact_with_DB import interact_db

# assignment10 blueprint definition
assignment10 = Blueprint('/assignment10', __name__,
                         static_folder='static', static_url_path='/assignment10',
                         template_folder='templates')


# ------------------------------------------------- #
# ------------------- SELECT ---------------------- #
# ------------------------------------------------- #

# Routes
@assignment10.route('/assignment10')
def index():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=users)


# ------------------------------------------------- #
# ------------------- INSERT ---------------------- #
# ------------------------------------------------- #

@assignment10.route('/insert_user', methods=['POST'])
def insert_user_func():
    # get the data
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    # insert to db
    query = "INSERT INTO users(name, email, password) VALUES ('%s', '%s', '%s');" % (name, email, password)
    interact_db(query=query, query_type='commit')

    # come back to users
    return redirect('/assignment10')


# ------------------------------------------------- #
# ------------------- DELETE ---------------------- #
# ------------------------------------------------- #

@assignment10.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['id']
    query = "DELETE FROM users WHERE id='%s';" % user_id
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')

# ------------------------------------------------- #
# ------------------- UPDATE ---------------------- #
# ------------------------------------------------- #

@assignment10.route('/update_user', methods=['GET','POST'])
def update_user_func():
    if request.method == 'POST':
        user_id = request.form['id']
        if request.form['name']:
            newName = request.form['name']
            query = "update users set name = '%s' where id ='%s';" % (newName, user_id)
            interact_db(query, query_type='commit')
        if request.form['email']:
            newEmail = request.form['email']
            query = "update users set email = '%s' where id ='%s';" % (newEmail, user_id)
            interact_db(query, query_type='commit')
        if request.form['password']:
            newPassword = request.form['password']
            query = "update users set password = '%s' where id ='%s';" % (newPassword, user_id)
            interact_db(query, query_type='commit')
        return redirect('/assignment10')
    return redirect('/assignment10')
