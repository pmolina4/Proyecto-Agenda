from typing import Callable # para agregar anotaciones a las clases

from flask_sqlalchemy import SQLAlchemy


def init_db(app) -> dict[str, Callable]:
    db = SQLAlchemy(app)
	
	
    # esta clase gestionará la tabla, hay que pasarle la clase base de
    # todos los modelos de Flask alchemy que es db.Model	
    class Contact(db.Model):
        __tablename__ = "contacts"

        uid = db.Column("id", db.Integer, primary_key=True)
        nick = db.Column(db.String(16))
        first_name = db.Column(db.String(128))
        last_name = db.Column(db.String(128))
        phone = db.Column(db.Integer())
        
    # -------------------------------------------------------------
    # Aquí se definirán las funciones que van a operar sobre la tabla (CRUD)
    # (create_contact, read_contact,update_contact, delete_contact, list_contacts)
    # -------------------------------------------------------------

    # create_all es un método de Flask-alchemy que crea la tabla con sus campos
    db.create_all() 

    return {}
