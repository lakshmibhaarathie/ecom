
import os
import logging
from api.constants.api_constants import get_current_time_stamp, LOGS_DIR

def get_log_file_name():
    return f"log_{get_current_time_stamp()}.log"

LOG_FILE_NAME = get_log_file_name()
os.makedirs(LOGS_DIR, exist_ok= True)
LOG_FILE_PATH = os.path.join(LOGS_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode="w",
    format='[%(asctime)s]:   %(levelname)s  %(lineno)s  %(filename)s  %(message)s',
    level=logging.INFO
    )
