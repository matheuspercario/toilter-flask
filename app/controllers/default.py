from flask import render_template
from app import app


# Página Index
@app.route('/index/')
@app.route('/',)
def index():
    return render_template('index.html',)


@app.route('/login/')
def login():
    return render_template('base.html')


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
