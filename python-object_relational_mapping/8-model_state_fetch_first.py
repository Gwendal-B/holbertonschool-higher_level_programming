#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa using SQLAlchemy ORM.
The first State is determined by the lowest id. If no State exists, prints 'Nothing'.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # MySQL credentials
    user, password, db = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, db),
                           pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the first state ordered by id
    first_state = session.query(State).order_by(State.id).first()

    # Display result
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()
