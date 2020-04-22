from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/index')
def index():

# return "Hello, World!"    # Tutorial 1.
    user = {'username': 'Chris'}
    posts = [
        {
            'author': {'username': 'Han'},
            'body': 'This is HanChengge'
        },
        {
            'author': {'username': 'Ho'},
            'body': 'This is HoJongChol'
        }
    ]
#     return '''
# <html>
#     <head>
#         <title>Home Page - Microblog</title>
#     </head>
#     <body>
#         <h1>Hello, ''' + user['username'] + '''!</h1>
#     </body>
# </html>'''
    return render_template('index.html', title='Home', user=user, posts=posts)       # Tutorial 2
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form = form)       # Tutorial 3

