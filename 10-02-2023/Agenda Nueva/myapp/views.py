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
    
    #-------------VIEW DE EQUIPO ---------------------
    @app.route("/", methods=["GET", "POST"])
    def index():
        # invoca a la clase mammal que está implementada en models.py con el método "list"
        # y luego lanza la vista "index.html"
        list_equipos = db_access["list"]
        equipos = list_equipos()  # para mostrar al inicio los contactos que ya están en la BD
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

    @app.route("/update/<int:equipo_id>", methods=["GET", "POST"])
    def update(equipo_id: int):
        if request.method == "GET":
            read_equipo = db_access["read"]
            equipo = read_equipo(equipo_id)
            return render_template("update.html", equipo=equipo)

        if request.method == "POST":
            update_equipo = db_access["update"]
            update_equipo(
                equipo_id=equipo_id,
                nombre=request.form["nombre"],
                ciudad=request.form["ciudad"],
                fundacion=request.form["fundacion"]
            )
            return redirect("/")

    @app.route("/delete/<int:equipo_id>", methods=["GET", "POST"])
    def delete(equipo_id: int):
        if request.method == "GET":
            read_equipo = db_access["read"]
            equipo = read_equipo(equipo_id)
            return render_template("delete.html", equipo=equipo)

        if request.method == "POST":
            delete_equipo = db_access["delete"]
            delete_equipo(
                equipo_id=equipo_id
            )
            return redirect("/")

    #-------------VIEW DE JUGADOR ---------------------

    @app.route("/jugador", methods=["GET", "POST"])
    def jugador():
        # invoca a la clase mammal que está implementada en models.py con el método "list"
        # y luego lanza la vista "index.html"
        list_jugador = db_access["list_filtrada"]
        # para mostrar al inicio los contactos que ya están en la BD
        jugadores = list_jugador()
    
        return render_template("jugador.html", jugadores=jugadores)

    @app.route("/create_jugador", methods=["GET", "POST"])
    def create_jugador():
        if request.method == "GET":
            list_equipos = db_access["list"]
            equipos = list_equipos()

            return render_template("create_jugador.html", equipos=equipos)
        
        if request.method == "POST":
            create_jugador = db_access["create_jugador"]
            create_jugador(
                nombre=request.form["nombre"],
                numero=request.form["numero"],
                posicion=request.form["posicion"],
                id_equipo=request.form["id_equipo"]
            )
            return redirect("/jugador")
     
    @app.route("/delete_jugador/<int:jugador_id>", methods=["GET", "POST"])
    def delete_jugador(jugador_id: int):
        if request.method == "GET":
            read_jugador = db_access["read_jugador"]
            jugador = read_jugador(jugador_id)
            return render_template("delete_jugador.html", jugador=jugador)

        if request.method == "POST":
            delete_jugador = db_access["delete_jugador"]
            delete_jugador(
                jugador_id=jugador_id
            )
            return redirect("/jugador")   
    
    @app.route("/update_jugador/<int:jugador_id>", methods=["GET", "POST"])
    def update_jugador(jugador_id: int):
        if request.method == "GET":
            read_jugador = db_access["read_jugador"]
            jugador = read_jugador(jugador_id)
            return render_template("update_jugador.html", jugador=jugador)

        if request.method == "POST":
            update_jugador = db_access["update_jugador"]
            update_jugador(
                jugador_id=jugador_id,
                Nombre=request.form["nombre"],
                Numero=request.form["numero"],
                Posicion=request.form["posicion"]
            )
            return redirect("/jugador")
    
    #-------------VIEW DE Lesion ---------------------

    @app.route("/lesion", methods=["GET", "POST"])
    def lesion():
        # invoca a la clase mammal que está implementada en models.py con el método "list"
        # y luego lanza la vista "index.html"
        list_lesion = db_access["list_lesion"]
        # para mostrar al inicio los contactos que ya están en la BD
        lesiones = list_lesion()
    
        return render_template("lesion.html", lesiones=lesiones)
    
    @app.route("/create_lesion", methods=["GET", "POST"])
    def create_lesion():
        if request.method == "GET":
            list_lesion = db_access["list_lesion"]
            lesiones = list_lesion()

            return render_template("create_lesion.html", lesiones=lesiones)
        
        if request.method == "POST":
            create_lesion = db_access["create_lesion"]
            create_lesion(
                nombre=request.form["lesion"],
                tiempo=request.form["tiempoRecuperacion"]
            )
            return redirect("/lesion")
        
    @app.route("/delete_lesion/<int:id>", methods=["GET", "POST"])
    def delete_lesion(id: int):
        if request.method == "GET":
            read_lesion = db_access["read_lesion"]
            lesion = read_lesion(id)
            return render_template("delete_lesion.html", lesion=lesion)

        if request.method == "POST":
            delete_lesion = db_access["delete_lesion"]
            delete_lesion(
                id=id
            )
            return redirect("/lesion")   
    
    @app.route("/update_lesion/<int:id>", methods=["GET", "POST"])
    def update_lesion(id: int):
        if request.method == "GET":
            read_lesion = db_access["read_lesion"]
            lesion = read_lesion(id)
            return render_template("update_lesion.html", lesion=lesion)

        if request.method == "POST":
            update_lesion = db_access["update_lesion"]
            update_lesion(
                id= id,
                Lesion=request.form["lesion"],
                TiempoRecuperacion=request.form["tiempo"]
            )
            return redirect("/lesion")