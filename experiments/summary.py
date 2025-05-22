import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables in a file called .env
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

