import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


from client import client

rekognition = client("rekognition")

response = rekognition.detect_moderation_labels(
    Image={
        "BytesPath": "images/sample.jpg"
    }
)

print("Moderation Results:")

if response["ModerationLabels"]:
    for label in response["ModerationLabels"]:
        print(
            label["Name"],
            label["Confidence"]
        )
else:
    print("No moderation labels detected.")
