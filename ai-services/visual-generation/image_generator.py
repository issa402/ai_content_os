import request
from config import API_KEY, IMAGE_MODEL

def generate_image(prompt):
	headers = {
		"Authorization": f"Bearer {API_KEY}",
		"Content_Type": "application/json"
	}
	
	payload = {
		"model": IMAGE_MODEL,
		"input":{
			"prompt" : prompt
		}
	}

	response = request.post(
		"https://dashscope-intl.aliyuncs.com/api/v1/services/aigc/text2image",
		headers = headers,
		json = payload
	)

	data = response.json()
	image_url = data["output"]["results"][0]["url"]
	return requests.get(image_url).content

