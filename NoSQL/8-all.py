#!/usr/bin/env python3
""" List all documents in Python """
from pymongo import MongoClient


def list_all(mongo_collection):
    """ Lists all documents in a collection """
    documents = mongo_collection.find({})
    for document in documents:
        return(document)
