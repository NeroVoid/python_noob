logs = [
  "2025-09-16 10:05:12 | user=alice | ip=192.168.1.10",
  "2025-09-16 10:06:03 | user=bob | ip=10.0.0.5",
]

print(f"{'User':<10} {'IP':<15}")

for log in logs:
    parts = log.split(" | ")
    user_name = parts[1]
    user_ip = parts[2]
    user = user_name.split("=")[1]
    ip = user_ip.split("=")[1]
    print(f"{user:<10} {ip:<15}")