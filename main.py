from flask import Flask
import requests
from google.cloud import storage
from datetime import datetime


app = Flask(__name__)

BUCKET_NAME = "sreenu-api-raw-bucket"

@app.route("/")
def ingest():

    url = "https://dummyjson.com/products?limit=100&skip=0"

    response = requests.get(url)

    client = storage.Client()

    bucket = client.bucket(BUCKET_NAME)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    blob = bucket.blob(
        f"raw/products_{timestamp}.json"
    )

    blob.upload_from_string(
        response.text,
        content_type="application/json"
    )

    return "Data loaded to GCS"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
