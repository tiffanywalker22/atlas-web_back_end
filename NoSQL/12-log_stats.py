#!/usr/bin/env python3
"""Write a Python script that provides some stats about
Nginx logs stored in MongoDB"""
from pymongo import MongoClient

def nginx_logs_stats():
    """script that provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx
    print("{} collection".format(collection.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print("\tmethod {}: {}".format(method,collection.count_documents({"method": method})))
    print("{} status check".format(collection.count_documentsP({"method": "GET", "path": "/status"})))

if __name__ == "__main__":
    nginx_logs_stats()