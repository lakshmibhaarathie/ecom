from datetime import datetime


def get_current_time_stamp():
    return f"{datetime.now().strftime(f'%Y-%m-%d-%H-%M-%S')}"

LOGS_DIR ="logs"

CURRENT_TIME_STAMP = get_current_time_stamp()