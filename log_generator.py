import time
import random
from datetime import datetime

LOG_FILE = "access.log"

STATUS_CODES = [200]*70 +  [301]*10 + [404]*15 + [500]*5

def generate_log_line():
    ip = f"192.168.1.{random.randint(1, 255)}"
    date = datetime.now().strftime("%d/%b/%Y:%H:%M:%S %z")
    method = random.choice(["GET", "POST", "PUT",])
    path= random.choice(["/index.html", "/about.html", "/contact.html", "/api/user", "/contact", "/login"])
    status = random.choice(STATUS_CODES)
    size = random.randint(100, 5000)
    return f'{ip} - - [{date}] "{method} {path} HTTP/1.1" {status} {size}'

print(f"Generating log file: {LOG_FILE}")
with open(LOG_FILE, "w") as f:
    while True:
        line = generate_log_line()
        f.write(line + "\n")
        f.flush()  # Ensure the line is written to the file immediately
        print(line)  # Print the generated log line to the console
        time.sleep(random.uniform(0.1, 1.0))  # Sleep for a random