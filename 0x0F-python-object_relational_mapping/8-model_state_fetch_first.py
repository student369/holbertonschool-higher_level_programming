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
    sql = "SELECT * FROM states ORDER BY states.id;"
    result = engine.execute(sql)
    state = result.fetchone()
    print("{:d}: {:s}".format(state.id, state.name))
