#!/usr/bin/python3
"""Module 12-model_state_update_id_2
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """ Main

    Update a state
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
    """
    sql = "SELECT * FROM states ORDER BY states.id;"
    result = engine.execute(sql)
    states = result.fetchall()
    result = engine.execute(states.insert(),
                   [{name: "Louisiana"}]
    )
    """
    states = State.__table__
    conn = engine.connect()
    stmt = states.update().where(
        states.c.id == 2
    ).values(name="New Mexico")
    conn.execute(stmt)
    conn.close()
