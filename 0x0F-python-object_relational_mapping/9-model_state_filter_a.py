#!/usr/bin/python3
"""List states from mysqldb that has letter a"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def list_states_with_letter_a():
    """This functin lists all state objects with
    the letter a.
    """

    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@localhost:3306/{db}'
            )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).\
        filter(State.name.like('%a%')).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    list_states_with_letter_a()
