from time import sleep

from src.app.scanner import run_scan_files
from src.app.copying import run_copy_cache_db
from src.settings import SCANN_PATH, SAVE_PATH, DEMON_INTERVAL
from src.app.ffmpeg_control import FFMPEGСonsole
from src.app.converter import run_convert_cache_db

from src.app.utilities.lock_file import check_lock_file, create_lock_file, del_lock_file


def run_demon_job():
    if not check_lock_file():
        try:
            create_lock_file()
            ffmpeg_console = FFMPEGСonsole()
            while check_lock_file():
                run_scan_files(SCANN_PATH, ffmpeg_console)
                run_convert_cache_db(SAVE_PATH, ffmpeg_console)
                run_copy_cache_db(SAVE_PATH)
                if DEMON_INTERVAL > 0:
                    sleep(DEMON_INTERVAL)
        finally:
            del_lock_file()
