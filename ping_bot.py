import time
import requests
from requests.exceptions import RequestException, ConnectionError, Timeout, HTTPError
import logging
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Setup logging
logging.basicConfig(
    filename="ping_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load URL from environment variable
url = os.getenv("PING_URL")

# Custom headers (optional)
headers = {
    "User-Agent": "DiscordBotPinger/1.0"
}

# Ping function
def ping_url(url, retries=3, backoff_factor=2):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # Raise error for bad status codes
            logging.info(f"Ping successful for {url}. Status Code: {response.status_code}")
            print(f"✅ Ping successful for {url} - Status: {response.status_code}")
            return
        except (HTTPError, ConnectionError, Timeout) as e:
            logging.error(f"Error pinging {url}: {e}")
            print(f"❌ Error pinging {url}: {e}")
            attempt += 1
            sleep_time = backoff_factor ** attempt  # Exponential backoff
            print(f"Retrying in {sleep_time} seconds...")
            time.sleep(sleep_time)
        except RequestException as e:
            logging.critical(f"Critical error for {url}: {e}")
            break

# Main loop to ping URL continuously
def start_pinging(interval=60):
    while True:
        ping_url(url)
        print(f"Sleeping for {interval} seconds before next ping...")
        time.sleep(interval)

if __name__ == "__main__":
    try:
        if not url:
            print("❌ Error: PING_URL not set in .env file.")
        else:
            start_pinging(interval=60)  # Ping every 60 seconds (adjust if needed)
    except KeyboardInterrupt:
        print("\nStopping the ping script.")
        logging.info("Ping script stopped by user.")
