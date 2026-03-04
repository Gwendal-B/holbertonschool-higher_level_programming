#!/usr/bin/python3
"""Prints the State object with a name passed as argument from the database
hbtn_0e_6_usa.

Displays the state.id if found, otherwise prints 'Not found'.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get arguments
    user, password, db_name, state_name = sys.argv[1], sys.argv[2],
    sys.argv[3], sys.argv[4]

    # Connect to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, db_name),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query state with given name (SQL injection safe)
    state = session.query(State).filter(State.name == state_name).first()

    # Print result
    if state:
        print(state.id)
    else:
        print("Not found")
