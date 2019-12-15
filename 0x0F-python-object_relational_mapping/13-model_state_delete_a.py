#!/usr/bin/python3
"""Module 13-model_state_delete_a
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """ Main

    Delete a state
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
    states = State.__table__
    conn = engine.connect()
    stmt = states.delete().where(
        states.c.name.like("%a%")
    )
    conn.execute(stmt)
    conn.close()
