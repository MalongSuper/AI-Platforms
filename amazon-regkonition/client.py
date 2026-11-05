# Create a Boto3-style client
# Instead of calling AWS directly, we create a small Python client that sends requests to Flask.
import requests


class LocalRekognition:

    def __init__(self, endpoint="http://127.0.0.1:5000"):
        self.endpoint = endpoint

    def _send_image(self, api, image_path):

        with open(image_path, "rb") as image:
            response = requests.post(
                f"{self.endpoint}/{api}",
                files={
                    "image": image
                }
            )

        response.raise_for_status()
        return response.json()

    def detect_labels(self, Image, **kwargs):
        return self._send_image(
            "detect_labels",
            Image["BytesPath"]
        )

    def detect_text(self, Image, **kwargs):
        return self._send_image(
            "detect_text",
            Image["BytesPath"]
        )

    def detect_moderation_labels(self, Image, **kwargs):
        return self._send_image(
            "detect_moderation_labels",
            Image["BytesPath"]
        )


def client(service_name, region_name=None):
    if service_name != "rekognition":
        raise ValueError("Unsupported service")

    return LocalRekognition()
