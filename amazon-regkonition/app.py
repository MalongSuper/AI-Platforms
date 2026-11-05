# app.py: This is the server that receives image requests and performs the analysis.
from flask import Flask, request, jsonify
import cv2
import numpy as np
import easyocr

app = Flask(__name__)

# Initialize OCR engine
reader = easyocr.Reader(['en'], gpu=False)


def read_image():
    file = request.files.get("image")

    if file is None:
        return None

    image_bytes = np.frombuffer(
        file.read(), np.uint8
    )

    return cv2.imdecode(
        image_bytes, cv2.IMREAD_COLOR
    )


# 1. Label Detection
@app.route("/detect_labels", methods=["POST"])
def detect_labels():
    image = read_image()

    if image is None:
        return jsonify({"error": "Invalid image"}), 400

    # Basic image analysis placeholder
    height, width = image.shape[:2]

    labels = [
        {
            "Name": "Image",
            "Confidence": 99.0
        },
        {
            "Name": "Object",
            "Confidence": 95.0
        }
    ]

    return jsonify({"Labels": labels})


# 2. Text Detection
@app.route("/detect_text", methods=["POST"])
def detect_text():
    image = read_image()

    if image is None:
        return jsonify({"error": "Invalid image"}), 400

    results = reader.readtext(image)

    detections = []

    for box, text, confidence in results:
        detections.append({
            "DetectedText": text,
            "Type": "LINE",
            "Confidence": round(confidence * 100, 2)
        })

    return jsonify({
        "TextDetections": detections
    })


# 3. Content Moderation
@app.route("/detect_moderation_labels", methods=["POST"])
def detect_moderation():
    image = read_image()

    if image is None:
        return jsonify({"error": "Invalid image"}), 400

    # Placeholder: no actual moderation model
    labels = []

    return jsonify({
        "ModerationLabels": labels
    })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
