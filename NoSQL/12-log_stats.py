#!/usr/bin/env python3
"""Write a Python script that provides some stats about
Nginx logs stored in MongoDB"""
from pymongo import MongoClient

def nginx_logs_stats():
    """script that provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    get_status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{get_status_count} logs with method=GET and path=/status")

if __name__ == "__main__":
    nginx_logs_stats()
