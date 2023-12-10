#!/usr/bin/python3
"""Base review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class review"""
    place_id = ""
    user_id = ""
    text = ""
