# import scrapy
import json
# import os

# from models import Author, Quote, Tag
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base
# from sqlalchemy.ext.declarative import declarative_base # this is for alchemy 1.x

import configparser
# import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


config = configparser.ConfigParser()
config.read('postgres.ini')

post_user = config.get('DEFAULT', 'user')
post_pass = config.get('DEFAULT', 'pass')
post_host = config.get('DEFAULT', 'host')
post_port = config.get('DEFAULT', 'port')
post_db = config.get('DEFAULT', 'db_name')

# ----- posgres connect -----
db_uri = f"""postgresql://{post_user}:{post_pass}@{post_host}:{post_port}/{post_db}"""
engine = create_engine(db_uri) 
# engine = create_engine(db_uri, echo=True) # for debug

DBSession = sessionmaker(bind=engine)
# session = DBSession() # this one should be closed, so we will call it in the main module

Base = declarative_base()

filename_quotes = "quotes.json"
filename_authors = "authors.json"

class Tag(Base):
    __tablename__ = 'quotes_tag'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, max_length=25, unique=True)
    # name = models.CharField(max_length=25, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"

class Quote(Base):
    __tablename__ = 'quotes_quote'
    # tags = models.ManyToManyField(Tag)
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, max_length=2000)
    tags = relationship('Tags', backref='quotes_quotes')
    # text = models.CharField(max_length=2000, null=False)

    def __str__(self):
        return f"{self.text}"

class Author(Base):
    __tablename__ = 'quotes_author'
    id = Column(Integer, primary_key=True, unique=True)
    fullname = Column(String, nullable=False, max_length=200)
    born_date = Column(String, nullable=False, max_length=200)
    born_location = Column(String, nullable=False, max_length=200)
    description = Column(String, nullable=False, max_length=2000)
    quote = relationship('Quote', backref='quotes_author')


    def __str__(self):
        return f"{self.fullname}"

def save_to_posgtres(session):

    def read_json(file):
        with open(file, "r", encoding='utf-8') as f:
            return json.load(f)

    # Author.drop_collection()
    # Quotes.drop_collection()

    authors = read_json(filename_authors)
    quotes = read_json(filename_quotes)

    for author in authors:
        session.add(Author(**author))

    for quote in quotes:
        author_name = Author.objects(fullname=quote['author']).first()
        quote['author'] = author_name
        session.add(Quotes(**quote))

    session.commit()

if __name__ == "__main__":
    session = connect_postgres.DBSession()
    save_to_posgtres(session)
    session.close()

