from typing import Callable # para agregar anotaciones a las clases

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Sequence


def init_db(app) -> dict[str, Callable]:
    db = SQLAlchemy(app)

    # esta clase gestionará la tabla, hay que pasarle la clase base de
    # todos los modelos de Flask alchemy que es db.Model
    class Alojamiento(db.Model):
        
        __tablename__ = "alojamiento" # nombre de la tabla creada en SQLite3
        # esto es para que la tabla no tome el nombre por defecto de la clase
        # en minúsculas

        # declarar campos de la tabla "mammals"
        id_alojamiento = db.Column("id_alojamiento", db.Integer, Sequence('id_alojamiento_seq'), primary_key=True)
        nombre = db.Column(db.String(5))
        n_habitaciones = db.Column(db.Integer())
        n_banos = db.Column(db.Integer())
        pax = db.Column(db.Integer())
        direccion = db.Column(db.String(30))

    # ------------- métodos que operan sobre el contenido la tabla -----------

    def list_alojamiento() -> list[Alojamiento]:
        alojamientos = Alojamiento.query.all()
        return [alojamiento for alojamiento in alojamientos]

    # create_all es un método de Flask-alchemy que crea la tabla con sus campos
    db.create_all()

    return {
        "list": list_alojamiento
    }
