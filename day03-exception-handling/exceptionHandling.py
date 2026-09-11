import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[logging.FileHandler("app_execution.log"), logging.StreamHandler(sys.stdout)])

error_count = 0
info_count = 0
warn_count = 0
total_count = 0

try:
    with open("app.log","r") as file:
        for line in file:
            clean_line = line.strip()
            if not clean_line:
                continue
            total_count += 1
            log_part = line.split(" ", 1)
            log_type = log_part[0]
            match log_type:
                case "ERROR":
                    error_count += 1
                    logging.error(f"Error log: {clean_line}")
                case "WARN":
                    warn_count += 1
                    logging.warning(f"Warning log: {clean_line}")
                case "INFO":
                    info_count += 1
                    logging.info(f"Info log: {clean_line}")
                case _:
                    logging.warning(f"Unknown log type: {clean_line}")

        logging.info(f"Execution Summart")
        logging.info(f"Total logs processed: {total_count}, Total errors: {error_count}, Total warnings: {warn_count}, Total info logs: {info_count}")

except FileNotFoundError:
    logging.error("File not found. Please check the file path.")
    sys.exit(1)
except PermissionError:
    logging.error("Permission denied. Please check the file permissions.")
    sys.exit(1)
