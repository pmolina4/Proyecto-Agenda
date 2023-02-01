from typing import Callable

from flask import redirect, render_template, request

# init_views inicializa la clase de las vistas
# app es un objeto flask creado en app.py (en app.py: app = Flask(__name__)
# db_access es el objeto que devuelve init_db para gestionar la base de datos (en app.py: db_access = init_db(app))
# ambos pasan como parámetros a init_views

def init_views(app, db_access: dict[str, Callable]): 
    # definición de las acciones a realizar para lanzar cada vista
    # nótese que el código de "/" no pregunta si se ha hecho una petición, así que deberá ejecutarse al inicializar
    # en el caso de los demás tienen sentencias IF para que el código se ejecute solo si haya una petición
    @app.route("/", methods=["GET", "POST"])
    def index():
    	# invoca a la clase mammal que está implementada en models.py con el método "list"
    	# y luego lanza la vista "index.html"
        list_equipos = db_access["list"] 
        equipos = list_equipos() # para mostrar al inicio los contactos que ya están en la BD
        return render_template("index.html", equipos=equipos)

    @app.route("/create", methods=["GET", "POST"])
    def create():
        if request.method == "GET":
            return render_template("create.html")

        if request.method == "POST":
            create_equipo = db_access["create"]
            create_equipo(
                nombre=request.form["nombre"],
                ciudad=request.form["ciudad"],
                fundacion=request.form["fundacion"]
            )
            return redirect("/")

    @app.route("/update/<int:uid>", methods=["GET", "POST"])
    def update(uid: int):
        if request.method == "GET":
            read_mammal = db_access["read"]
            mammal = read_mammal(uid)
            return render_template("update.html", mammal=mammal)

        if request.method == "POST":
            update_mammal = db_access["update"]
            update_mammal(
                uid=uid,
                genus=request.form["genus"],
                sex=request.form["sex"],
                plot_type=request.form["plot_type"],
                hindfoot_length=int(request.form["hindfoot_length"]),
            )
            return redirect("/")

    @app.route("/delete/<int:uid>", methods=["GET", "POST"])
    def delete(uid: int):
        if request.method == "GET":
            read_mammal = db_access["read"]
            mammal = read_mammal(uid)
            return render_template("delete.html", mammal=mammal)

        if request.method == "POST":
            delete_mammal = db_access["delete"]
            delete_mammal(
                uid=uid,
            )
            return redirect("/")
