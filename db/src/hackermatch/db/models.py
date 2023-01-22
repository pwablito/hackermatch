from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


# BEGIN HACKERMATCH TABLES

class Submission(Base):
    __tablename__ = "submission"

    id = Column(Integer, primary_key=True)
    hash = Column(String)
    email = Column(String)

# END HACKERMATCH TABLES
