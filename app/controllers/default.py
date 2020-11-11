from app import app

# Teste hello world
@app.route("/hello/")
def hello():
    return "Hello World!"

# Teste Index
@app.route("/index/")
@app.route("/")
def index():
    return "Index Page"

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