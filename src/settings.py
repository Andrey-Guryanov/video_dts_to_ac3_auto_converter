from typing import Final
from pathlib import Path
from src.app.utilities.yml_handler import read_yaml

WORK_DIR = Path.cwd()
DB_CACHE_NAME: Final[str] = "file_cache.db"
CONFIG: Final[dict] = read_yaml(WORK_DIR / "config.yaml")
DB_CACHE_DIR: Final[Path] = WORK_DIR / "src" / "db_cache"
LOG_DIR: Final[Path] = WORK_DIR / "src" / "logs" / "log.log"

if CONFIG:
    SAVE_PATH: Final[Path] = Path(CONFIG["save_path"])
    SCANN_PATH: Final[Path] = Path(CONFIG["scann_path"])
    SAVE_STRUCT: Final[bool] = CONFIG["save_structure"]
    COPY_ALL: Final[bool] = CONFIG["copy_all"]
else:
    SAVE_PATH = None
    SCANN_PATH = None
    SAVE_STRUCT = None
    COPY_ALL = None

DAEMON_INTERVAL: Final[int] = 60

LOG_LEVEL: Final[str] = "DEBUG"
LOG_ROTATION: Final[int] = 1
