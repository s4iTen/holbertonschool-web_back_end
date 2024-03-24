#!/usr/bin/env python3
"""school topics"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """10. Change school topics"""
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )