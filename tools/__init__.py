import os 
from dotenv import load_dotenv

load_dotenv()

BROWSERLESS_API_KEY=os.environ.get("BROWSERLESS_API_KEY")
SERPER_API_KEY=os.environ.get("SERPER_API_KEY")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")
APIFY_KEY=os.environ.get("APIFY_KEY")
