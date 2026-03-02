import os 
from dotevn import load_dotenv

load_dotenv()

API_KEY = os.getenv("AI_APIKEY")

VIDEO_URL = "https://dashscope-intl.aliyuncs.com/api/v1/services/aigc/video-generation/video-synthesis"
TASK_STATUS_URL = "https://dashscope-intl.aliyuncs.com/api/v1/tasks"
IMAGE_MODEL = "qwen-image-max"
VIDEO_MODEL = "wan-image-to-video"