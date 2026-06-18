from flask import Flask
import requests
from google.cloud import storage

app = Flask(__name__)

BUCKET_NAME = "sreenu-raw-data-bucket"

@app.route("/")
def ingest():

    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    client = storage.Client()

    bucket = client.bucket(BUCKET_NAME)

    blob = bucket.blob("raw/posts.json")

    blob.upload_from_string(
        response.text,
        content_type="application/json"
    )

    return "Data loaded to GCS"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
