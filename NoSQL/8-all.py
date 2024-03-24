#!/usr/bin/env python3
""" List documents """
import pymongo


def list_all(mongo_collection):
    """8. List all documents in Python"""
    docs = []
    for doc in mongo_collection.find():
        docs.append(doc)
    return docs