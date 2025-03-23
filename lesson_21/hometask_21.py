import logging
from datetime import datetime

# Налаштування логера
log_filename = "hb_test.log"
logging.basicConfig(
    filename=log_filename,
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Шлях до вхідного файлу
input_filename = "hblog.txt"

# Фільтруємо рядки з ключем
key_filter = "Key TSTFEED0300|7E3E|0400"

def extract_timestamp(log_line):
    """ Витягує час з рядка логів """
    timestamp_index = log_line.find("Timestamp ")
    if timestamp_index != -1:
        return log_line[timestamp_index + 10: timestamp_index + 18]
    return None

# Читаємо файл та фільтруємо лише потрібні рядки
filtered_logs = []
with open(input_filename, "r", encoding="utf-8") as file:
    for line in file:
        if key_filter in line:
            timestamp = extract_timestamp(line)
            if timestamp:
                filtered_logs.append((timestamp, line.strip()))

# Аналіз heartbeat
if len(filtered_logs) > 1:
    for i in range(len(filtered_logs) - 1):
        t1 = datetime.strptime(filtered_logs[i][0], "%H:%M:%S")
        t2 = datetime.strptime(filtered_logs[i + 1][0], "%H:%M:%S")
        heartbeat_diff = (t1 - t2).total_seconds()

        if 31 <= heartbeat_diff < 33:
            logging.warning(f"Heartbeat {heartbeat_diff} sec at {filtered_logs[i][0]}")
        elif heartbeat_diff >= 33:
            logging.error(f"Heartbeat {heartbeat_diff} sec at {filtered_logs[i][0]}")

print(f"Аналіз завершено. Результати у {log_filename}")
