import pickle
import os.path
from time import time
from src.settings import WORK_DIR

PATH_LOCK = WORK_DIR / "STOP"


def check_lock_file() -> bool:
    if os.path.isfile(PATH_LOCK):
        return True
    return False


def create_lock_file() -> None:
    with open(PATH_LOCK, "wb+") as lock_file:
        pickle.dump(time(), lock_file)


def del_lock_file() -> None:
    if check_lock_file():
        os.remove(PATH_LOCK)
