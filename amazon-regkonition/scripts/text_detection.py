import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from client import client

rekognition = client("rekognition")

response = rekognition.detect_text(
    Image={
        "BytesPath": "images/sample.jpg"
    }
)

print("Detected Text:")

for detection in response["TextDetections"]:
    print(
        detection["DetectedText"],
        detection["Confidence"]
    )
