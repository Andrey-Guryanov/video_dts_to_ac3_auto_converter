from typing import Optional, List
from peewee import IntegrityError
from pathlib import Path

from src.app.utilities.log import logger
from .model import db, FileHistory, BaseModel


class DB_Services(object):
    def __init__(self):
        db.connect()

    def init(self):
        FileHistory.create_table()
        self._del_all_rows()

    def add_file(
        self,
        file_hash: str,
        file_name: str,
        file_path: Path,
        convert_status: bool,
        file_size,
    ) -> None:
        new_file = FileHistory(
            file_hash=file_hash,
            file_name=file_name,
            file_path=str(file_path),
            convert_status=convert_status,
            file_size=file_size,
        )
        if self._save_db(new_file):
            logger.info("Add new file = {}", file_path)

    @staticmethod
    def get_no_convert(limit_count: int = 10) -> Optional[List]:
        query = FileHistory.select().where(FileHistory.convert_status == False).limit(10)
        result = [value for value in query]
        if result:
            return result
        return

    @staticmethod
    def get_no_copy(limit_count: int = 10) -> Optional[List]:
        query = (
            FileHistory.select()
            .where(
                (FileHistory.copy_status == False) & (FileHistory.convert_status == True)
            )
            .limit(10)
        )
        result = [value for value in query]
        if result:
            return result
        return

    @staticmethod
    def check_file(file_hash: str) -> bool:
        query = FileHistory.select().where(FileHistory.file_hash == file_hash)
        if query.exists():
            return True
        return False

    @staticmethod
    def _save_db(new_row: BaseModel) -> None:
        try:
            new_row.save()
            return True
        except IntegrityError:
            return False

    @staticmethod
    def _del_all_rows():
        query = FileHistory.delete()
        query.execute()


DB_MANAGER = DB_Services()
