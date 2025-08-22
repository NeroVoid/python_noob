logs_2 = [
    "# system boot",
    "2025-08-21T09:00:00Z,alice,SUCCESS",
    "2025-08-21T09:01:00Z,bob,FAIL",
    "2025-08-21T09:01:10Z,bob,FAIL",
    "2025-08-21T09:01:20Z,bob,FAIL",
    "2025-08-21T09:01:30Z,bob,FAIL",
    "2025-08-21T09:01:30Z,bob,FAIL",
    "",
    "2025-08-21T09:01:30Z,bob,FAIL",
    "2025-08-21T09:01:40Z,carol,SUCCESS",
    "2025-08-21T09:01:50Z,bob,FAIL",
    "END",
    "2025-08-21T09:02:00Z,alice,FAIL",
]

attempts = {}
consecutive_fails = {}

for log in logs_2:
    if log.startswith("#"):
        continue
    if log == "END":
        break
    if log.strip() == "":
        continue

    parts = log.split(",")
    user = parts[1]
    status = parts[2]
    
    if user not in attempts:
        attempts[user] = {"SUCCESS": 0, "FAIL": 0}
        consecutive_fails[user] = 0

    if status == "SUCCESS":
        attempts[user]["SUCCESS"] +=1
        consecutive_fails[user] = 0

    if status == "FAIL":
        attempts[user]["FAIL"] +=1
        consecutive_fails[user] +=1
        if consecutive_fails[user] == 5:
            print(f"ALERT: Too many consecutive failed attempts.")
            break 

print(f"User login attempts report:")
for user, status in attempts.items():
    print(f"User: {user} \n"
          f"Success: {status["SUCCESS"]} \n"
          f"Fail: {status["FAIL"]} \n"
          "----------")