#!/usr/bin/python3
"""Module 9-model_state_filter_a.py
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """ Main

    Get the States by a n letter using SQLAlchemy
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
        if 'a' in s.name:
            print("{:d}: {:s}".format(s.id, s.name))
