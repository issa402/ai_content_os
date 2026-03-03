from image_generator import generate_image
from video_generator import generate_video
from storage import save_image, save_video, encode_image
from approval import ask_for_approval
import requests

prompt = input("Enter image prompt: ")

# 1 Generate image
image_binary = generate_image(prompt)

# 2 Save image
image_path = save_image(image_binary)

# 3 Ask approval
approved = ask_for_approval(image_path)

if not approved:
    print("Regenerate with new prompt.")
    exit()

# 4 Encode
encoded = encode_image(image_path)

# 5 Generate video
video_url = generate_video(encoded, "Cinematic motion")

# 6 Download video
video_binary = requests.get(video_url).content
final_path = save_video(video_binary)

print("Final video saved at:", final_path)















from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    # TODO: Implement health check logic
    return {"status": "Visual Generation service is healthy"}

@app.post("/generate-image")
def generate_image(prompt: str):
    # TODO: Implement image generation logic
    return {"image_url": f"https://example.com/image.jpg"}


# Reference Implementation
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from . import qwen_utils
from . import cropping

app = FastAPI()

class ImageRequest(BaseModel):
    prompt: str
    style: str = "default"

@app.get("/health")
def health_check():
    return {"status": "Visual Generation service is healthy"}

@app.post("/generate-image")
def generate_image(request: ImageRequest):
    try:
        # Generate image using Qwen
        image_path = qwen_utils.generate_image_with_qwen(request.prompt, request.style)

        # Crop the image
        cropped_image_path = cropping.crop_image(image_path)

        # TODO: Upload the cropped image to a storage service and return the URL
        return {"image_url": cropped_image_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""
