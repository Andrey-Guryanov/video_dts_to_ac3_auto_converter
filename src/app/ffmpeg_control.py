import json
from pathlib import Path
from src.app.utilities.command import console_execute, ErrorComandConsole


def check_ffmpeg_sys():
    console_args = ["ffmpeg", "-version"]
    result = console_execute(console_args).success
    return result


class FFMPEGСonsole(object):
    def __init__(self):
        self.sys_status: bool = check_ffmpeg_sys()

    @staticmethod
    def check_dts_codec(file_path: Path) -> bool:
        console_file_path = str(file_path)
        console_args = [
            "ffprobe",
            "-show_format",
            "-show_streams",
            "-of",
            "json",
            console_file_path,
        ]
        console_data = console_execute(console_args, True)
        metadata_info = json.loads(console_data.result.decode("utf-8"))
        if metadata_info:
            for data in metadata_info["streams"]:
                if data["codec_type"] == "audio" and data["codec_name"] == "dts":
                    return True
        return False

    @staticmethod
    def convert_mkv_dts_to_as(file_path: Path, save_path: Path):
        console_file_path = str(file_path)
        console_save_path = str(save_path)
        console_args = [
            "ffmpeg",
            "-i",
            console_file_path,
            "-map",
            "0",
            "-vcodec",
            "copy",
            "-scodec",
            "copy",
            "-acodec",
            "ac3",
            "-b:a",
            "640k",
            console_save_path,
        ]
        try:
            console_execute(console_args, True)
        except ErrorComandConsole as erorrs:
            print("Ошибка выполнения команды в консоле")
            raise erorrs
        except Exception as erorrs:
            print(f"Ошибка = {erorrs}")
            raise erorrs
