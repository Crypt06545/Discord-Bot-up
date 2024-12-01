# Discord Bot Uptime Pinger

This is a simple yet robust Python script designed to keep your Discord bot or web service online by continuously pinging a specified URL. It logs the status of each request and implements retry logic with exponential backoff in case of failures. Ideal for hosting environments like Render or similar services where continuous uptime is crucial.

---

## Features

- **Continuous Pinging**: Sends regular GET requests to ensure the bot remains online.
- **Retry Mechanism**: Automatically retries failed pings with exponential backoff.
- **Logging**: Logs all ping attempts and errors in a `ping_log.log` file.
- **Error Handling**: Handles HTTP errors, connection issues, timeouts, and other exceptions.
- **Custom Headers**: Uses a customizable `User-Agent` header.

---

## Getting Started

### Prerequisites

Ensure you have Python installed and the `requests` library:

```bash
pip install requests
```
