import time
import re
import requests

LOG_FILE = "access.log"
ERROR_THRESHOLD = 5
TIME_WINDOW = 60  # seconds
TG_TOKEN = "YOUR_TELEGRAM_BOT"
TG_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

def send_alert(message):
    url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    data = {
        "chat_id": TG_CHAT_ID,
        "text": f"ALERT: {message}"}
    try: 
        requests.post(url, data=data)
        print("Alert sent to Telegram")
    except Exception as e:
        print(f"Failed to send alert: {e}")    

def monitor():
    f = open(LOG_FILE, "r")
    f.seek(0, 2) 

    error_timestamps = []

    print("Log Warden started, monitoring for errors...")

    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue

        match = re.search(r'"\s(\d{3})\s', line)
        if match:
            status_code = int(match.group(1))
            if 400 <= status_code < 600:
                now = time.time()
                error_timestamps.append(now)
                print(f"Error detected: {status_code} at {time.ctime(now)}")

                error_timestamps = [t for t in error_timestamps if now - t <= TIME_WINDOW]

                if len(error_timestamps) >= ERROR_THRESHOLD:
                    msg = f"Limit of {ERROR_THRESHOLD} errors exceeded in the last {TIME_WINDOW} seconds!"
                    send_alert(msg)
                    error_timestamps = []

if __name__ == "__main__":
    monitor()