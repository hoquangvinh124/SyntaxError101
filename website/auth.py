from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__) 

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)

        if username != 'syntaxerror101' or password != '12345678':
            flash('Invalid credentials. Please try again.', category='error')

    return render_template("login.html")

@auth.route('/logout')
def logout():
    return 'Logout'

@auth.route('/sign-up')
def sign_up():
    return 'Sign Up'