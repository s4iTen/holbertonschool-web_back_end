#!/usr/bin/env python3
""" SQLAlchemy model """
from sqlalchemy import Column, Integer, String


# Define the User class
class User():
    """ SQLAlchemy model """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    hashed_password = Column(String(255), nullable=False)
    session_id = Column(String(255), nullable=False)
    reset_token = Column(String(255), nullable=False)
