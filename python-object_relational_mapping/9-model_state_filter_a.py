#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' from the
database hbtn_0e_6_usa.
Results are sorted in ascending order by states.id.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Arguments: mysql username, mysql password, database name
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, db_name),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states containing 'a'
    states_with_a = (
        session.query(State).filter(State.name.like('%a%'))
        .order_by(State.id).all()
    )

    # Print results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")
