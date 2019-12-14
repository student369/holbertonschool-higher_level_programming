#!/usr/bin/python3
"""Module 7-model_state_fetch_all
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """ Main

    Get the States using SQLAlchemy
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
    states = result.fetchall()
    for s in states:
        print("{:d}: {:s}".format(s.id, s.name))
