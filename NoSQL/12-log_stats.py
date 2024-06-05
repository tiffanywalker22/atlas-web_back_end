#!/usr/bin/env python3
"""Write a Python script that provides some stats about
Nginx logs stored in MongoDB"""
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.logs
collection = db.nginx


def nginx_logs_stats():
    """script that provides some stats about Nginx logs stored in MongoDB"""
    log_count = collection.count_documents({})
    print(f"{log_count} collections")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(f"\tmethod {method}: {collection.count_documents({'method': method})}")
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    nginx_logs_stats()