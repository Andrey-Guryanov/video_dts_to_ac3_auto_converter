import os
import mimetypes
from pathlib import Path

from src.model import DB_MANAGER
from src.app.utilities.hash import create_path_hash
from src.app.utilities.free_file import check_free_file

from .ffmpeg_control import FFMPEGСonsole


def run_scan_files(dir_path: Path, ffmpeg_console: FFMPEGСonsole) -> None:
    scan_files = os.walk(dir_path, topdown=True, onerror=None, followlinks=False)
    for path_root, _, files in scan_files:
        for file_name in files:
            file_path = Path(f"{path_root}/{file_name}")
            if check_video(file_path):
                if check_free_file(file_path):
                    file_hash = create_path_hash(file_path)
                    if file_name[-4:] == ".mkv" and check_convert(
                        file_path, ffmpeg_console
                    ):
                        convert_status = False
                    else:
                        convert_status = True
                    DB_MANAGER.add_file(
                        file_hash=file_hash,
                        file_name=file_name,
                        file_path=file_path,
                        convert_status=convert_status,
                    )


def check_video(file_path: Path) -> bool:
    file_type = mimetypes.guess_type(file_path)
    if file_type[0]:
        return file_type[0].startswith("video")
    return False


def check_convert(file_path: Path, ffmpeg_console: FFMPEGСonsole) -> None:
    return ffmpeg_console.check_dts_codec(file_path)
