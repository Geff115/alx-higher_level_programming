#!/usr/bin/python3
"""Script to delete state from db"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def delete_state_with_letter_a():
    """This functin deletes all State objects with name
    containing the letter a.
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

    """ This deletes a state name starting with 'a' in the db """
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    delete_state_with_letter_a()
