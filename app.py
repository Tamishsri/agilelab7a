import datetime

print("Hello, World!")

now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Timestamp: {timestamp}")
