from flask import Flask, render_template_string
from threading import Thread
from dotenv import load_dotenv
import ping_bot
import sys

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bot Uptime Monitor</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #1e1e1e;
                color: #f5f5f5;
                text-align: center;
                padding: 20px;
            }
            h1 {
                font-size: 2.5em;
                margin: 20px 0;
            }
            p {
                font-size: 1.5em;
            }
        </style>
    </head>
    <body>
        <h1>Bot Uptime Monitor</h1>
        <p>Status: <strong>{{ status }}</strong></p>
        <p>Last Checked: <strong>{{ last_checked }}</strong></p>
    </body>
    </html>
    """
    return render_template_string(
        html_template,
        status=ping_bot.status_message,
        last_checked=ping_bot.last_checked
    )

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
