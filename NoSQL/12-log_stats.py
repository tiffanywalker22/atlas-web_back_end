#!/usr/bin/env python3
"""Write a Python script that provides some stats about
Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def nginx_logs_stats():
    """script that provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient()
    db = client.logs
    logs = db.nginx
    log_count = logs.count_documents({})
    print(f"{log_count} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(f"\tmethod {method}: {logs.count_documents({'method': method})}")
    status_check_count = logs.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    nginx_logs_stats()