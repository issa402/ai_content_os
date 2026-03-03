import requests
import time
from config import API_KEY, VIDEO_URL, TASK_STATUS_URL, VIDEO_MODEL

def generate_video(encoded_image, prompt):
	headers = {
		"Authorization": f"Bearer {API_KEY}",
		"Content-Type": "application/json"
	}

	payload = {
		"model": VIDEO_MODEL,
		"input": {
			"image": encode_image,
			"prompt": prompt
		}
	}

	response = request.post(VIDEO_URL,headers = headers, json = payload)
	task_id = response.json()["output"]["task_id"]

	while True:
        result = requests.get(f"{TASK_STATUS_URL}/{task_id}", headers=headers).json()
        status = result["output"]["task_status"]

        if status == "SUCCEEDED":
            return result["output"]["video_url"]

        if status == "FAILED":
            raise Exception("Video generation failed")

        time.sleep(10)
