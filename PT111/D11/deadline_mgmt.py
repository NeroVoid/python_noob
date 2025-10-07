from datetime import datetime, timedelta

tasks = [
    ["Submit report", 3],
    ["Prepare slides", 5],
    ["Team meeting", 1]
]
now = datetime.now()
for task in tasks:
    task_name, days_to_finish = task
    deadline = now + timedelta(days=days_to_finish)
    print(f"{task_name} - Deadline: {deadline.strftime('%Y-%m-%d')}")