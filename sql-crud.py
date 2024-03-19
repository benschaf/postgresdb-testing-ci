from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")
base = declarative_base()


class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

try:
    ada_lovelace = Programmer(
        first_name = "Ada",
        last_name = "Lovelace",
        gender = "F",
        nationality = "British",
        famous_for = "First Programmer"
    )

    ben = Programmer(
        first_name = "Benjamin",
        last_name = "Schäfer",
        gender = "M",
        nationality = "Deutsch",
        famous_for = "awesomeness"
    )

    people = session.query(Programmer)
    for person in people:
        if person.gender == "Female":
            person.gender = "female"
        elif person.gender == "Male":
            person.gender = "male"
        else:
            print("Gender not defined")

    programmer = session.query(Programmer).filter_by(id = 2).first()
    session.delete(programmer)
    # programmer.famous_for = "World President"
    # session.add(ben)
    # session.add(ada_lovelace)
    session.commit()



except Exception as e:
    print(f"Error: {e}")

try:
    programmers = session.query(Programmer)
    for programmer in programmers:
        print(
            programmer.id,
            programmer.first_name + " " + programmer.last_name,
            programmer.gender,
            programmer.nationality,
            programmer.famous_for,
            sep = " | "
        )
except Exception as e:
    print(f"Error: {e}")