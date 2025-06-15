#!/usr/bin/env python3
""" Insert a document in Python """
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based on kwargs """
    
