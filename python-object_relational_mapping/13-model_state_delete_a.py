#!/usr/bin/python3
"""Delete all State objects containing the letter 'a' from the database."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Récupération des arguments
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Création de l'engine SQLAlchemy
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, password, db_name),
                           pool_pre_ping=True)

    # Création d'une session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Suppression des états contenant 'a'
    states_to_delete = session.query(State).filter(State.name
                                                   .like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    # Fermeture de la session
    session.close()
