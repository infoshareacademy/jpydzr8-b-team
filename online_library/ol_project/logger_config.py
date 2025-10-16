# import logging
#
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s [%(levelname)s] %(message)s",
#     filename="online_library.log",
#     filemode="a"  # dopisywanie do pliku
# )
# logger = logging.getLogger(__name__)

import logging
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Tworzymy własny logger "myapp"
logger = logging.getLogger('online_library')
logger.setLevel(logging.INFO)
logger.propagate = False  # <- bardzo ważne, nie przesyłaj logów dalej do root loggera

# Handler do pliku
file_handler = logging.FileHandler(os.path.join(BASE_DIR, 'online_library.log'), mode='a')
file_handler.setLevel(logging.INFO)

# Format logów
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(formatter)

# Dodajemy handler do loggera
logger.addHandler(file_handler)
