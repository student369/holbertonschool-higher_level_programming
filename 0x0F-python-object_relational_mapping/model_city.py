#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module model_state

This module contains the State class

"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """City class

    A simple model City class
    """
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"),
                      nullable=False)
