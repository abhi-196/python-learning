info_count = 0
error_count = 0
warning_count = 0
unknown_count = 0

with open("app.log", "r") as file:
    for line in file:
        content = line.strip()
        if content.startswith("ERROR"):
            error_count += 1
            print(f"Error log found: {content}")
        elif content.startswith("WARN"):
            warning_count += 1
            print(f"Warning log found: {content}")
        elif content.startswith("INFO"):
            info_count += 1
            print(f"Info log found: {content}")
        elif content.startswith("UNKNOWN"):
            unknown_count += 1
            print(f"Unknown log found: {content}")

print(f"total errors: {error_count}")
print(f"total warnings: {warning_count}")
print(f"total info count: {info_count}") 
print(f"total unknown count: {unknown_count}")
    
