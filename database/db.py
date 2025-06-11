from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base

engine = create_engine('sqlite:///sudoku.db', echo=False)
Session = sessionmaker(bind=engine)

def init_db():
    from database import models 
    Base.metadata.create_all(engine)
