import os
import shutil
from pathlib import Path

from src.model import DB_MANAGER
from src.app.utilities.log import logger
from src.settings import SAVE_STRUCT, SCANN_PATH, SAVE_PATH
from src.app.utilities.dir_path import crete_dir_structure


def run_copy_cache_db(save_path_dir: Path):
    logger.debug("Run copy new files")
    while True:
        new_files = DB_MANAGER.get_no_copy()
        if new_files:
            for new_file in new_files:
                file_path = Path(new_file.file_path)
                if SAVE_STRUCT:
                    save_path = crete_dir_structure(SCANN_PATH, file_path, SAVE_PATH)
                    save_path = save_path / new_file.file_name
                else:
                    save_path = save_path_dir / new_file.file_name
                if file_path != save_path:
                    if not os.path.isfile(save_path):
                        logger.info("Start copy file = {}", file_path)
                        shutil.copyfile(file_path, save_path)
                        logger.info("End copy file, save = {}", save_path)
                    else:
                        logger.info("File already exists, path = {}", save_path)
                new_file.copy_status = True
                new_file.save()
        else:
            logger.debug("No new file copy")
            break
