#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Retrieve MySQL credentials and database name
    user, password, db = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create a SQLAlchemy engine
    engine = (
        create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                      .format(user, password, db), pool_pre_ping=True)
    )

    # Create a configured "Session" class and a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch all State objects ordered by id
    states = session.query(State).order_by(State.id).all()

    # Print each state
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
