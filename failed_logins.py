from collections import defaultdict

THRESHOLD = 2
LOG_FILE = "auth.log.py"

failed_attempts = defaultdict(int)

with open(LOG_FILE, "r") as f:
    for line in f:
        line = line.strip()

        if "Failed login" in line:
            ip = line.split()[-1]
            failed_attempts[ip] += 1

print("Suspicious IPs (failed attempts >= threshold):")
for ip, count in failed_attempts.items():
    if count >= THRESHOLD:
        print(f"{ip} - {count} failed attempts")
