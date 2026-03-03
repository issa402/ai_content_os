import os
import bas64
from datetime import datetime

TMP_DIR = "../../tmp"
OUT_DIR = "../../outputs"

os.makedir(TMP_DIR, exist_ok = true)
os.makedir(OUT_DIR, exist_ok = true)

def save_image(content):
	filename = f"{TMP_DIR}/image_{datetime.now().timestamp()}.png"
	with open(filename, "wb"), as f:
		f.write(content)
	return filename

def save_video(content):
	filename  = f"{OUT_DIR}/image_{datetime.now().timestamp()}.png"
	with open(filename, "wb") as f:
		f.write(content)
	return filename

def encode_image(path):
	with open(path, "rb") as img:
		return base64.b64encode(img.read()).decode()

