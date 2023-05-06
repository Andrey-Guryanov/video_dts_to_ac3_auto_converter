import os
from pathlib import Path
from datetime import datetime


def check_free_file(file_path: Path):
    if not file_path.exists():
        raise FileNotFoundError
    try:
        file_path.rename(file_path)
    except PermissionError:
        return False
    else:
        file_stat = os.stat(file_path)
        datetime_now = datetime.now()
        datetime_modified = datetime.fromtimestamp(file_stat.st_mtime)
        if (datetime_now - datetime_modified).seconds > 10:
            return True
    return False
