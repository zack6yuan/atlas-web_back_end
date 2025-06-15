#!/usr/bin/env python3
""" List all documents in Python """
from pymongo import MongoClient


def list_all(mongo_collection):
    """ Lists all documents in a collection """
    document_list = []
    documents = mongo_collection.find({})
    for document in documents:
        document_list.append(document)
    return document_list
