#!/usr/bin/env python3
""" Change school topics """
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """ update topics function """
    