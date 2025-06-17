#!/usr/bin/env python3
""" List of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """ Schools by topic function """
    topics_list = []
    topics = mongo_collection.find(
        {"topics": topic}
    )
    for topic in topics:
        topics_list.append(topic)
    return topics_list
