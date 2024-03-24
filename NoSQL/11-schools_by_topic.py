#!/usr/bin/env python3
""" 11-main """
import pymongo


def schools_by_topic(mongo_collection, topic):
    """11. Where can I learn Python?"""
    specific_topic = mongo_collection.find({ "topics": topic })
    to_list = list(specific_topic)
    return to_list