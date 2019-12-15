#!/usr/bin/python3
"""Module 8-model_state_fetch_first.py
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """ Main

    Get the first State using SQLAlchemy
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(
            sys.argv[1], sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmake(bind=engine)
    sess = Session()
    state = sess.query(State).first()
    if state:
        print("{:d}: {:s}".format(state.id, state.name))
    else:
        print("Nothing")
