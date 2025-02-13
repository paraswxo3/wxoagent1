from elasticsearch import Elasticsearch
import requests

# Connect to Elasticsearch
api_key = "SC15ai1wUUJ4cEc3QzVEYms0OWw6Vlp1Y0RKQzNSbzJsU0VBZUFyQmxRQQ=="
cloud_id = "my_deployment:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyQwOWI5MmM5NWEzNzI0OWQyODE4M2UzMGY3OWQxOGEwMSQwYWFjYzAyZmExNTk0ZTFiOTNiMmI3NzhkZTIyMWYyMw=="
es =  Elasticsearch(
    "https://070e4c0d4e8c4aee93f3a029e9711984.us-central1.gcp.cloud.es.io:443",
    api_key=api_key
)
# print(es.info())


# es.ingest.put_pipeline(
#     id="elser-ingest-pipeline",
#     description="Ingest pipeline for ELSER",
#     processors=[
#         {
#             "inference": {
#                 "model_id": ".elser_model_2_linux-x86_64",
#                 "input_output": [
#                     {"input_field": "content", "output_field": "content_embedding"}
#                 ],
#             }
#         }
#     ],
# )

es.indices.delete(index="bank_guarantee_clauses", ignore_unavailable=True)
es.indices.create(
    index="bank_guarantee_clauses",
    settings={"index": {"default_pipeline": "elser-ingest-pipeline"}},
    mappings={
        "properties": {
            "content": {"type": "text"},
            "content_embedding": {"type": "sparse_vector"},
            "clause": {"type": "text"}
        }
    }
)