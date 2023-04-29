import click

from src.settings import SCANN_PATH, SAVE_PATH
from src.app.scanner import run_scan_files
from src.app.demon import run_demon_job
from src.app.copying import run_copy_cache_db
from src.app.converter import run_convert_cache_db
from src.app.ffmpeg_control import FFMPEGСonsole
from src.app.command_menu import init_config, init_start_job


@click.group()
def cli():
    ...


@cli.command
def init() -> None:
    init_config()


@cli.command
def run_demon():
    if init_start_job():
        run_demon_job()


@cli.command
def run_convert_cache():
    if init_start_job():
        ffmpeg_console = FFMPEGСonsole()
        run_convert_cache_db(SAVE_PATH, ffmpeg_console)


@cli.command
def run_copy_cache():
    init_start_job()
    run_copy_cache_db(SAVE_PATH)


@cli.command
def run_sacn():
    if init_start_job():
        ffmpeg_console = FFMPEGСonsole()
        run_scan_files(SCANN_PATH, ffmpeg_console)


if __name__ == "__main__":
    cli()
