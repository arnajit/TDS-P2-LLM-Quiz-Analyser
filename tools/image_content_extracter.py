from langchain.tools import tool
from google import genai
from io import BytesIO
from PIL import Image
import base64
import requests
import os

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def load_image_bytes(image_input):
    """Convert URL / file path / base64 / bytes into raw PNG bytes."""
    # Base64 input
    if isinstance(image_input, str) and image_input.startswith("data:"):
        _, b64 = image_input.split(",", 1)
        return base64.b64decode(b64)

    # URL input
    if isinstance(image_input, str) and (image_input.startswith("http://") or image_input.startswith("https://")):
        resp = requests.get(image_input, timeout=10)
        resp.raise_for_status()
        return resp.content

    # Local path (inside LLMFiles)
    if isinstance(image_input, str):
        with open(os.path.join("LLMFiles", image_input), "rb") as f:
            return f.read()

    # Raw bytes
    if isinstance(image_input, bytes):
        return image_input

    # PIL image
    if isinstance(image_input, Image.Image):
        buf = BytesIO()
        image_input.save(buf, format="PNG")
        return buf.getvalue()

    raise ValueError("Unsupported image input type")


@tool
def ocr_image_tool(payload: dict) -> dict:
    """
    Extract text from an image using Gemini Vision.
    Payload:
    {
        "image": ... (url, bytes, base64, file path, PIL),
        "prompt": "your instruction"
    }
    """
    try:
        img_bytes = load_image_bytes(payload["image"])
        img_b64 = base64.b64encode(img_bytes).decode("utf-8")

        prompt = payload.get("prompt", "Extract all text from this image.")

        result = client.models.generate_content(
            model="gemini-2.5-flash",
            contents={
                "role": "user",
                "parts": [
                    {
                        "inline_data": {
                            "mime_type": "image/png",
                            "data": img_b64
                        }
                    },
                    {
                        "text": prompt
                    }
                ]
            }
        )

        # Gemini may return result.text or result.candidates
        text = None
        if hasattr(result, "text"):
            text = result.text
        else:
            text = result.candidates[0].content.parts[0].text

        return {"text": text.strip(), "engine": "gemini-vision"}

    except Exception as e:
        return {"error": str(e), "engine": "gemini-vision"}
