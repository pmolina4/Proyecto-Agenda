from typing import Callable # para agregar anotaciones a las clases

from flask_sqlalchemy import SQLAlchemy


def init_db(app) -> dict[str, Callable]:
    db = SQLAlchemy(app)

    # esta clase gestionará la tabla, hay que pasarle la clase base de
    # todos los modelos de Flask alchemy que es db.Model
    class Mammal(db.Model):
        
        __tablename__ = "species" # nombre de la tabla creada en SQLite3
        # esto es para que la tabla no tome el nombre por defecto de la clase
        # en minúsculas

        # declarar campos de la tabla "mammals"
        uid = db.Column("id", db.Integer, primary_key=True)
        genus = db.Column(db.String(16))
        sex = db.Column(db.String(128))
        plot_type = db.Column(db.String(128))
        hindfoot_length = db.Column(db.Integer())

        # __str__ es un método especial para que al hacer un print del objeto nos devuelva 
        # el id, nombre y apellido 
        def __str__(self): 
            return f"[{self.uid}] {self.genus} {self.sex}"

        # utilizar el decorador  property para crear una propiedad (atributo) de la clase
        # al que es posible referirse para directamente obtener los atributos nombre y apellido de una vez 
        @property
        def fullname(self) -> str:
            return f"{self.genus} {self.sex}"

    # ------------- métodos que operan sobre el contenido la tabla -----------
    def create_mammal(genus: str, sex: str, plot_type: str, hindfoot_length: int):
        mammal = Mammal(
            genus=genus, sex=sex, plot_type=plot_type, hindfoot_length=hindfoot_length
        )
        db.session.add(mammal)
        db.session.commit()

    def read_mammal(uid: int) -> Mammal:
        return Mammal.query.get(uid)

    def update_mammal(
        uid: int, genus: str, sex: str, plot_type: str, hindfoot_length: int
    ):
        mammal = Mammal.query.get(uid)
        mammal.genus = genus
        mammal.sex = sex
        mammal.plot_type = plot_type
        mammal.hindfoot_length = hindfoot_length
        db.session.commit()

    def delete_mammal(uid: int):
        mammal = Mammal.query.get(uid)
        db.session.delete(mammal)
        db.session.commit()

    def list_mammals() -> list[Mammal]:
        mammals = Mammal.query.all()
        return [mammal for mammal in mammals]

    # create_all es un método de Flask-alchemy que crea la tabla con sus campos
    db.create_all()

    return {
    	# estos alias serán usados para llamar a los métodos de la clase, por ejemplo db_access["create"]
    	# invoca al método create_contact
        "create": create_mammal,
        "read": read_mammal,
        "update": update_mammal,
        "delete": delete_mammal,
        "list": list_mammals,
    }


# a = contacts(
#     nick="iderator", first_name="Roberto", last_name="Becerra", phone=657365440
# )

# db.session.add(a)
# db.session.commit()
