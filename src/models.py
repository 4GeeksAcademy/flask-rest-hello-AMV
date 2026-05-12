import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100))
    email = Column(String(100), unique=True, nullable=False)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    image_url = Column(String(250), nullable=False)
    caption = Column(String(500))
    # Relación: Un post pertenece a un usuario
    user = relationship(User)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(1000), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    # Relaciones: Un comentario tiene un autor y pertenece a un post
    author = relationship(User)
    post = relationship(Post)


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))


# Generación del diagrama
try:
    render_er(Base, 'diagram.png')
    print("¡Éxito! El diagrama ha sido generado en diagram.png")
except Exception as e:
    print("Hubo un error generando el diagrama:")
    print(e)
