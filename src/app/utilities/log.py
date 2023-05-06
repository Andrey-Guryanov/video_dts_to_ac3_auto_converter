from loguru import logger
from src.settings import LOG_LEVEL, LOG_ROTATION, LOG_DIR

logger.add(
    LOG_DIR,
    format="{time:DD-MM-YYYY HH:mm:ss:SSS}  {file}  {function}  {line}  {level} -> {message}",
    level=LOG_LEVEL,
    rotation=f"{LOG_ROTATION} MB",
    compression="zip",
)
