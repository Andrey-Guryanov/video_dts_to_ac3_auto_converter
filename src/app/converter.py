import os
from pathlib import Path
from datetime import datetime
from src.model import DB_MANAGER
from src.app.ffmpeg_control import FFMPEGСonsole
from src.app.utilities.dir_path import crete_dir_structure
from src.settings import SAVE_STRUCT, SCANN_PATH, SAVE_PATH


def run_convert_cache_db(save_path_dir: Path, ffmpeg_console: FFMPEGСonsole):
    while True:
        file_replace = False
        new_files = DB_MANAGER.get_no_convert()
        if new_files:
            for new_file in new_files:
                file_path = Path(new_file.file_path)
                save_path = save_path_dir / new_file.file_name
                if file_path == save_path:
                    file_replace = True
                    save_path = save_path_dir / f"temp__{new_file.file_name}"
                else:
                    if SAVE_STRUCT:
                        save_path = crete_dir_structure(SCANN_PATH, file_path, SAVE_PATH)
                        save_path = save_path / new_file.file_name
                _conerter_dts_to_ac(ffmpeg_console, file_path, save_path)
                if file_replace:
                    os.remove(file_path)
                    os.rename(save_path, str(save_path_dir / new_file.file_name))
                new_file.convert_status = True
                new_file.copy_status = True
                new_file.conver_ddt = datetime.now()
                new_file.save()
        else:
            break


def _conerter_dts_to_ac(ffmpeg_console, file_path: Path, save_path: Path):
    ffmpeg_console.convert_mkv_dts_to_as(file_path, save_path)
