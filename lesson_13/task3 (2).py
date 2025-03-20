import logging
import xml.etree.ElementTree as ET

# Налаштування логера
log_filename = 'xml_instructor.log'
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Парсинг XML-файлу
xml_file_path = "xml/groups.xml"

try:
    tree = ET.parse(xml_file_path)  # Парсинг XML-файлу
    root = tree.getroot()  # Кореневий елемент

    found_any = False  # Прапорець для перевірки, чи знайдено хоч одне значення

    for group in root.findall("group"):
        number = group.find("number")
        if number is not None:
            timing = group.find("timingExbytes/incoming")
            if timing is not None:
                logger.info(f"Для group/number={number.text} знайдено incoming: {timing.text}")
                print(f"Значення incoming для group/number={number.text}: {timing.text}")
                found_any = True

    if not found_any:
        logger.info("Жодного значення incoming не знайдено.")
        print("Жодного значення incoming не знайдено.")

except ET.ParseError as e:
    logger.error(f"Помилка парсингу XML файлу {xml_file_path}: {e}")
    print(f"Помилка парсингу XML файлу {xml_file_path}: {e}")
except Exception as e:
    logger.error(f"Невідома помилка під час обробки файлу {xml_file_path}: {e}")
    print(f"Невідома помилка під час обробки файлу {xml_file_path}: {e}")
