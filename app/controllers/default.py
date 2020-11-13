from flask import render_template, redirect, url_for
from sqlalchemy.orm import query
from app import app, db


from app.models.forms import LoginForm
from app.models.tables import User


# Página Index
@app.route('/index/')
@app.route('/',)
def index():
    return render_template('index.html',)


@app.route('/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        return redirect(url_for('login')) # clear form
    else:
        print(form.errors)
    return render_template('login.html', form=form)


@app.route('/insert/', defaults={'info' : None})
@app.route('/insert/<info>/')
def insert(info):
    user = User('teste', '123', 'Testers Test', 'test@example.com')
    db.session.add(user)
    db.session.commit()
    return 'OK'


@app.route('/select/', defaults={'username' : None})
@app.route('/select/<username>/')
def select(username):
    if username == 'all':
        users = User.query.all()
    elif username:
        users = User.query.filter_by(username=username).all()
    else:
        users = User.query.order_by(User.username).all()
    return render_template('show_users.html', users=users)

# ------------------------------------------------------------
# TESTES -----------------------------------------------------

# Teste hello world
@app.route("/hello/")
def hello():
    return """
    <html>
    <head>
        <title>Hello world</title>
    </head>
    <body>
        <h1>Hello world!</h1>
    </body>
    </html>
    """


# Teste parâmetro
@app.route("/test/", defaults={'name': None})
@app.route("/test/<name>/")
def test(name):
    if name:
        return f"Olá, {name}!"
    else:
        return f"Olá, usuário!"

# Teste parâmetro numérico


@app.route("/test2/<int:id>/")
def test2(id):
    return f"O ID é {id}"
