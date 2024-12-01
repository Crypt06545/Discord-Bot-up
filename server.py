from flask import Flask
from threading import Thread
from dotenv import load_dotenv
import ping_bot
import time
import signal
import sys

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return f"<h1>{ping_bot.status_message}</h1>"

def run_ping_bot():
    try:
        ping_bot.start_pinging(interval=60)
    except KeyboardInterrupt:
        print("\nPinging stopped.")
        sys.exit(0)

if __name__ == "__main__":
    # Start the pinging in a separate thread
    t = Thread(target=run_ping_bot)
    t.start()

    # Start the Flask web server
    try:
        app.run(host="0.0.0.0", port=5000)
    except KeyboardInterrupt:
        print("\nFlask server stopped.")
        sys.exit(0)
