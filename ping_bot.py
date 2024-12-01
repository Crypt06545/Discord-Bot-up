import time
import requests
import logging
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(
    filename="ping_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

url = os.getenv("PING_URL")
status_message = "Uptime Monitor Running"

def ping_url(url, retries=3, backoff_factor=2):
    attempt = 0
    global status_message
    while attempt < retries:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            status_message = f"✅ Ping successful! Status: {response.status_code}"
            logging.info(status_message)
            print(status_message)
            return
        except requests.exceptions.RequestException as e:
            attempt += 1
            sleep_time = backoff_factor ** attempt
            status_message = f"❌ Ping failed: {e}. Retrying in {sleep_time} seconds..."
            logging.error(status_message)
            print(status_message)
            time.sleep(sleep_time)

def start_pinging(interval=60):
    global status_message
    while True:
        if url:
            ping_url(url)
        else:
            status_message = "No URL set in environment!"
        time.sleep(interval)
