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
        jugadores = db.relationship('Jugador', back_populates='equipo', lazy='dynamic')
     
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
        equipo = db.relationship('Equipo', back_populates='jugadores')
 
        def __str__(self):
            return f"[{self.Nombre}] {self.Numero} {self.Posicion}"        

   # ------------- FUNCIONES DE EQUIPO -----------
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
    
    #------------FUNCIONES JUGADORES ---------------
    """
    Esta Funcion lo que devuelve es los jugadores con sus campos 
    de forma normal es decir el id id_equipo y todo segun esta metido
    en la bd
    """
    def list_jugador() -> list[Jugador]:
        Jugadores = Jugador.query.all()
        return [Jugador for Jugador in Jugadores] 
    '''
    Esta funcion lo uqe hace es que gaurdo la información de la bd en un array
    y además el id_equipo  lo comparo con el equipo que es y lo guardo 
    en el array para después poder mostrarlo en la tabla 
    ya que el usuario no sabría por el id_equipo a que equipo corresponde
    '''
    def list_jugadores() -> list[Jugador]:
        jugadores = Jugador.query.all()
        result = []
        for jugador in jugadores:
            jugador_dict = jugador.__dict__
            if jugador.equipo:
                jugador_dict['equipo'] = jugador.equipo.nombre
            else:
                jugador_dict['equipo'] = None
            result.append(jugador_dict)
        return result
    
    def create_jugador(nombre: str, numero: int, posicion: str, id_equipo: str):
        jugador = Jugador(
            Nombre=nombre, Numero=numero, Posicion=posicion, id_equipo=id_equipo
        )
        db.session.add(jugador)
        db.session.commit()
        
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
        "list_jugadores": list_jugador,
        "list_filtrada" : list_jugadores,
        "create_jugador" : create_jugador
        }
