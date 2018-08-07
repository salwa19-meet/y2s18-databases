from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name, year, country):
    article_opject =    Knowledge(
        name=name,
        year=year,
        country=country)
    session.add(article_opject)
    session.commit()


    

def query_all_articles():
    knowledge = session.query(
       Knowledge).all()
    return knowledge

 
    

def query_article_by_topic():

    knowledge = session.query(knowledge).filter_by(topic = topic).first()
    return knowledge
    

def delete_article_by_topic():
    
    knowledge = session.query(knowledge).filter_by(topic = topic).delete()
    session.commit()
    

def delete_all_articles():
    knowledge = session.query(knowledge).all().delete()
    session.commit()


def edit_article_rating(topic, rating):
    article_opject = session.query(knowledge).filter_by(topic = topic).first()
    article_opject_rating = new_rating
    session.commit()
        


add_article("pizza", 1698 , "itali") 
print(query_all_articles())  





