from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd

engine = create_engine('sqlite:///dbfifa.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    Name = Column(String)
    Nation = Column(String)
    Club = Column(String)
    Position = Column(String)
    Age = Column(Integer)
    Overall = Column(Integer)
    Pace = Column(Integer)
    Shooting = Column(Integer)
    Passing = Column(Integer)
    Dribbling = Column(Integer)
    Defending = Column(Integer)
    Physicality = Column(Integer)
    Acceleration = Column(Integer)
    Sprint = Column(Integer)
    Positioning = Column(Integer)
    Finishing = Column(Integer)
    Shot = Column(Integer)
    Long = Column(Integer)
    Volleys = Column(Integer)
    Penalties = Column(Integer)
    Vision = Column(Integer)
    Crossing = Column(Integer)
    Free = Column(Integer)
    Curve = Column(Integer)
    Agility = Column(Integer)
    Balance = Column(Integer)
    Reactions = Column(Integer)
    Ball = Column(Integer)
    Composure = Column(Integer)
    Interceptions = Column(Integer)
    Heading = Column(Integer)
    Def = Column(Integer)
    Standing = Column(Integer)
    Sliding = Column(Integer)
    Jumping = Column(Integer)
    Stamina = Column(Integer)
    Strength = Column(Integer)
    Aggression = Column(Integer)
    Att_work_rate = Column(String)
    Def_work_rate = Column(String)
    Preferred_foot = Column(String)
    Weak_foot = Column(Integer)
    Skill_moves = Column(Integer)
    URL = Column(String)
    Gender = Column(String)
    GK = Column(Integer)

    def __repr__(self):
        return [{
            'id': self.id,
            'Name': self.Name,
            'Nation': self.Nation,
            'Club': self.Club,
            'Position': self.Position,
            'Age': self.Age,
            'Overall': self.Overall,
            'Pace': self.Pace,
            'Shooting': self.Shooting,
            'Passing': self.Passing,
            'Dribbling': self.Dribbling,
            'Defending': self.Defending,
            'Physicality': self.Physicality,
            'Acceleration': self.Acceleration,
            'Sprint': self.Sprint,
            'Positioning': self.Positioning,
            'Finishing': self.Finishing,
            'Shot': self.Shot,
            'Long': self.Long,
            'Volleys': self.Volleys,
            'Penalties': self.Penalties,
            'Vision': self.Vision,
            'Crossing': self.Crossing,
            'Free': self.Free,
            'Curve': self.Curve,
            'Agility': self.Agility,
            'Balance': self.Balance,
            'Reactions': self.Reactions,
            'Ball': self.Ball,
            'Composure': self.Composure,
            'Interceptions': self.Interceptions,
            'Heading': self.Heading,
            'Def': self.Def,
            'Standing': self.Standing,
            'Sliding': self.Sliding,
            'Jumping': self.Jumping,
            'Stamina': self.Stamina,
            'Strength': self.Strength,
            'Aggression': self.Aggression,
            'Att_work_rate': self.Att_work_rate,
            'Def_work_rate': self.Def_work_rate,
            'Preferred_foot': self.Preferred_foot,
            'Weak_foot': self.Weak_foot,
            'Skill_moves': self.Skill_moves,
            'URL': self.URL,
            'Gender': self.Gender,
            'GK': self.GK
        }]
        

def init_db():
    Base.metadata.create_all(bind=engine)
    df = pd.read_csv('./data/male_players.csv')
    df.to_sql('players', engine, if_exists='replace', index=False)



if __name__ == '__main__':
    init_db()
