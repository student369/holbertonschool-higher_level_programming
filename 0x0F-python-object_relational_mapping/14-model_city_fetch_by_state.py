#!/usr/bin/python3
"""Module 14-model_city_fetch_by_state.py
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
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
    Session = sessionmaker(bind=engine)
    sess = Session()
    sql = sess.query(State, City).filter(
        State.id == City.state_id
    )
    states = sql.all()
    for s in states:
        print("{:s}: ({:d}) {:s}".format(
            s.State.name,
            s.City.id,
            s.City.name)
        )
    sess.close()
