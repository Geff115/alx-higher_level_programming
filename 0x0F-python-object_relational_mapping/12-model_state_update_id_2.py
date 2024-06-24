#!/usr/bin/python3
"""Script to update state db"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def changes_statename_from_db():
    """Changes state object from the database hbtn_0e_6_usa."""

    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db}'
        )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.id == 2).all()
    if states:
        states[0].name = "New Mexico"
    session.commit()
    session.close()


if __name__ == "__main__":
    changes_statename_from_db()
