#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module model_state

This module contains the State class

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class

    A simple model State class
    """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
