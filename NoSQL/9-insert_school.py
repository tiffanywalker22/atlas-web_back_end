#!/usr/bin/env python3
"""Write a Python function that inserts a new document in a collection based
on kwargs"""

def insert_school(mongo_collection, **kwargs):
    """function that inserts a newdocument in a collection"""
    result_id = mongo_collection.insert_one(kwargs)
    return result_id.inserted_id
