import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    comment = relationship('Comment', backref='user', lazy=True)
    post = relationship('Post', backref='user', lazy=True)
    follower = relationship('Follower', backref='user', lazy=True)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    from_id = Column(Integer, ForeignKey('user.id'))
    from_user = relationship(User, foreign_keys=[from_id])
    to_id = Column(Integer, ForeignKey('user.id'))
    to_user = relationship(User, foreign_keys=[to_id])

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = relationship('Comment', backref='post', lazy=True)
    media = relationship('Media', backref='post', lazy=True)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))

    def to_dict(self):
        return {}

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e

