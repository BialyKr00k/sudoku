from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime
from sqlalchemy import Text

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    email = Column(String, unique = True, nullable = False)
    username = Column(String, unique = True, nullable = False)
    date_of_birth = Column(Date, nullable = False)
    hashed_password = Column(String, nullable = False)

    results = relationship("GameResult", back_populates = "user")

class GameResult(Base):
    __tablename__ = 'game_results'

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    difficulty = Column(String)
    score = Column(Integer)
    time_seconds = Column(Integer)
    timestamp = Column(DateTime, default = datetime.datetime.utcnow)

    user = relationship("User", back_populates = "results")

class SudokuBoard(Base):
    __tablename__ = 'sudoku_boards'

    id = Column(Integer, primary_key = True)
    difficulty = Column(String, nullable = False)
    board_data = Column(Text, nullable = False)
    solution_data = Column(Text, nullable = False)