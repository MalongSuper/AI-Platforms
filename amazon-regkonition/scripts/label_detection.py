import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from client import client

rekognition = client("rekognition")

response = rekognition.detect_labels(
    Image={
        "BytesPath": "images/sample.jpg"
    }
)

print("Detected Labels:")

for label in response["Labels"]:
    print(
        label["Name"],
        label["Confidence"]
    )
