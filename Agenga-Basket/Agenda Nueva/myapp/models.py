from typing import Callable  # para agregar anotaciones a las clases

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Sequence


def init_db(app) -> dict[str, Callable]:
    db = SQLAlchemy(app)

    # esta clase gestionará la tabla, hay que pasarle la clase base de
    # todos los modelos de Flask alchemy que es db.Model
    class Equipo(db.Model):

        __tablename__ = "Equipo"  # Nombre de la tabla que se crea

        # declarar campos de la tabla "Equipo"
        equipo_id = db.Column("equipo_id", db.Integer, Sequence(
            'equipo_id_seq'),  primary_key=True)
        nombre = db.Column(db.String(30))
        ciudad = db.Column(db.String(30))
        fundacion = db.Column(db.Integer)

        # __str__ es un método especial para que al hacer un print del objeto nos devuelva
        # el nombre, ciudad y fundacion
        def __str__(self):
            return f"[{self.nombre}] {self.ciudad} {self.fundacion}"



    class Jugador(db.Model):

        __tablename__ = "Jugador"  # Nombre de la tabla que se crea

        # declarar campos de la tabla "Equipo"
        jugador_id = db.Column("Jugador_id", db.Integer, Sequence(
            'Jugador_id_seq'),  primary_key=True)
        Nombre = db.Column(db.String(30))
        Numero = db.Column(db.String(30))
        Posicion = db.Column(db.Integer)
        id_equipo = db.Column(db.Integer, db.ForeignKey(
            "Equipo.equipo_id"), nullable=False)
        # __str__ es un método especial para que al hacer un print del objeto nos devuelva
        # el nombre, ciudad y fundacion
        def __str__(self):
            return f"[{self.Nombre}] {self.Numero} {self.Posicion}"        

   # ------------- métodos que operan sobre el contenido la tabla equipo -----------
    def create_equipo(nombre: str, ciudad: str, fundacion: int):
        equipo = Equipo(
            nombre=nombre, ciudad=ciudad, fundacion=fundacion
        )
        db.session.add(equipo)
        db.session.commit()

    def read_equipo(equipo_id: int) -> Equipo:
        return Equipo.query.get(equipo_id)

    def update_equipo(
        equipo_id: int, nombre: str, ciudad: str, fundacion: int
    ):
        equipo = Equipo.query.get(equipo_id)
        equipo.nombre = nombre
        equipo.ciudad = ciudad
        equipo.fundacion = fundacion
        db.session.commit()

    def delete_equipo(equipo_id: int):
        equipo = Equipo.query.get(equipo_id)
        db.session.delete(equipo)
        db.session.commit()

    def list_equipos() -> list[Equipo]:
        equipos = Equipo.query.all()
        return [equipo for equipo in equipos]

    def list_jugador() -> list[Jugador]:
        Jugadores = Jugador.query.all()
        return [Jugador for jugador in Jugadores] 

    # create_all es un método de Flask-alchemy que crea la tabla con sus campos
    db.create_all()

    return {
        # estos alias serán usados para llamar a los métodos de la clase, por ejemplo db_access["create"]
        # invoca al método create_contact
        "create": create_equipo,
        "read": read_equipo,
        "update": update_equipo,
        "delete": delete_equipo,
        "list": list_equipos,
        "list_jugadores": list_jugador
    }
