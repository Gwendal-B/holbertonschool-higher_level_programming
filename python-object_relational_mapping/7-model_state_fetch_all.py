#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user, password, db = sys.argv[1], sys.argv[2], sys.argv[3]

    # Créer le moteur de connexion
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête : récupérer tous les State triés par id
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()