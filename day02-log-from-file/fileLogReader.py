info_count = 0
error_count = 0
warning_count = 0
unknown_count = 0
total_logs = 0

with open("app.log", "r") as file:
        for line in file:
             clean_line = line.strip()
             if not clean_line:
                  continue  # Skip empty lines

             total_logs += 1

             log_part = line.split(" ", 1)
             log_type = log_part[0]

             match log_type:
                case "ERROR":
                    error_count +=1
                    print(f"❌ {clean_line}")
                case "WARN":
                    warning_count +=1
                    print(f"⚠️ {clean_line}")
                case "INFO":
                    info_count +=1
                    print(f"ℹ️ {clean_line}")
                case _:
                    unknown_count +=1
                    print(f"❓ {clean_line}")

print(f"total errors: {error_count}")
print(f"total warnings: {warning_count}")
print(f"total info count: {info_count}") 
print(f"total unknown count: {unknown_count}")