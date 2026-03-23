#!/usr/bin/python3
"""Change the name of the State with id = 2 to 'New Mexico' in the database."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get arguments
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, password, db_name),
                           pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the state with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
