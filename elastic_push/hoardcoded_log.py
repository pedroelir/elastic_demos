import time
from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch(['http://localhost:9200'])

# Define the index name
index_name = 'log_index'

# Example log data
log_data = [
    {"timestamp": "2024-03-07T12:00:00", "message": "Error: Disk space low"},
    {"timestamp": "2024-03-07T12:01:00", "message": "Warning: CPU usage high"},
    {"timestamp": "2024-03-07T12:02:00", "message": "Info: Application started"},
    # Add more log entries here
]

# Index log data into Elasticsearch
for entry in log_data:
    es.index(index=index_name, body=entry)

# Example search query
search_query = {
    "query": {
        "match": {
            "message": "Error"
        }
    }
}

time.sleep(3)
# Execute search query
search_results = es.search(index=index_name, body=search_query)

# Print search results
print("Search Results:")
for hit in search_results['hits']['hits']:
    print(f"Timestamp: {hit['_source']['timestamp']}, Message: {hit['_source']['message']}")
