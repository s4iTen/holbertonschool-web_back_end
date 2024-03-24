#!/usr/bin/env python3
"""12-log_stats"""
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['logs']
collection = db['nginx']

# Count total logs
total_logs = collection.count_documents({})

print(f"Total logs: {total_logs}")

# Count logs by method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in methods}

print("Methods:")
for method, count in method_counts.items():
    print(f"\t{method}: {count}")

# Count logs with method=GET and path=/status
status_count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"GET /status: {status_count}")
