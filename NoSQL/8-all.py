#!/usr/bin/env python3
from pymongo import MongoClient


def list_all(mongo_collection):
    """ Lists all databases in a collection """
    documents = mongo_collection.find({})
    for document in documents:
        return(document)
