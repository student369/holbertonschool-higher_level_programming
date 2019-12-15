#!/usr/bin/python3
"""Module 14-model_city_fetch_by_state.py
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
    sql = "SELECT s.name, c.id, c.name FROM states AS s \
INNER JOIN cities AS c ON c.state_id = s.id ORDER BY s.name;"
    result = engine.execute(sql)
    states = result.fetchall()
    for s in states:
        print("{:s}: ({:d}) {:s}".format(s[0], s[1], s[2]))
