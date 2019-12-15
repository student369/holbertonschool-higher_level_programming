#!/usr/bin/python3
"""Module 11-model_state_insert.py
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """ Main

    Insert a new state
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(
            sys.argv[1], sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )
    sname = sys.argv[3]
    Base.metadata.create_all(engine)
    """
    sql = "SELECT * FROM states ORDER BY states.id;"
    result = engine.execute(sql)
    states = result.fetchall()
    result = engine.execute(states.insert(),
                   [{name: "Louisiana"}]
    )
    """
    states = State.__table__
    ins = states.insert()
    ins = states.insert().values(name="Louisiana")
    conn = engine.connect()
    result = conn.execute(ins)
    print(result.inserted_primary_key[0])
    conn.close()
