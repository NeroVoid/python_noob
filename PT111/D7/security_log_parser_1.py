#This code is part of a security log parser that processes login logs to count successful and failed login attempts per user, and detects suspicious activity.

logs_1 = [
    "# system boot",
    "2025-08-21T09:00:00Z,alice,SUCCESS",
    "2025-08-21T09:01:00Z,bob,FAIL",
    "2025-08-21T09:01:10Z,bob,FAIL",
    "2025-08-21T09:01:20Z,bob,FAIL",
    "",
    "2025-08-21T09:01:30Z,bob,FAIL",
    "2025-08-21T09:01:40Z,carol,SUCCESS",
    "2025-08-21T09:01:50Z,bob,FAIL",
    "END",
    "2025-08-21T09:02:00Z,alice,FAIL",
]

attempts = {} # Track total login attempts per user
consecutive_fails = {} # Track consecutive failed login per user

for log in logs_1:
    if log.startswith("#"):
        continue
    if log == "END":
        break
    if log.strip() == "":
        continue
    
    parts = log.split(",")
    user = parts[1]
    status = parts[2]

    # Initialize user stats if not present
    if user not in attempts:
        attempts[user] = {"SUCCESS": 0, "FAIL": 0}
        consecutive_fails[user] = 0

    if status == "SUCCESS":
        attempts[user]["SUCCESS"] += 1
        consecutive_fails[user] = 0  # Reset on success

    elif status == "FAIL":
        attempts[user]["FAIL"] += 1
        consecutive_fails[user] += 1
        if consecutive_fails[user] == 5:
            print(f"ALERT: Too many consecutive failed attempts for user {user}.")
            break

print(f"User login attempts report:")
for user, status in attempts.items():
    print(f"User: {user} \n"
          f"Success: {status["SUCCESS"]} - Fail: {status["FAIL"]} \n"
          "----------")