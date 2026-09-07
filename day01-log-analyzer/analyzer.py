logs = [
    "INFO User service started",
    "ERROR Database connection timeout",
    "INFO Request completed",
    "WARN Kafka consumer lag is high",
    "ERROR Failed to publish event",
]

error_count = 0
warning_count = 0
info_count = 0

for log in logs:
    if log.startswith("ERROR"):
        error_count += 1
        print(f"Error log found: {log}")
    elif log.startswith("WARN"):
        warning_count += 1
        print(f"Warning log found: {log}")
    elif log.startswith("INF"):
        info_count += 1


print(f"Total errors: {error_count}")
print(f"Total warnings: {warning_count}")
print(f"Total info count : {info_count}")