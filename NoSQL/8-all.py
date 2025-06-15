#!/usr/bin/env python3
""" List all documents in Python """
from pymongo import MongoClient


def list_all(mongo_collection):
    """ Lists all documents in a collection """
    document_list = []
    document = mongo_collection.find({})
    if document:
        document.append(document_list)
    return document_list
