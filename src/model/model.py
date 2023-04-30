import os
from peewee import (
    Model,
    SqliteDatabase,
    PrimaryKeyField,
    CharField,
    BooleanField,
    DateTimeField,
    IntegerField,
)
from src.settings import DB_CACHE_NAME, DB_CACHE_DIR

if not os.path.exists(DB_CACHE_DIR):
    os.makedirs(DB_CACHE_DIR)

db = SqliteDatabase(DB_CACHE_DIR / DB_CACHE_NAME)


class BaseModel(Model):
    class Meta:
        database = db


class FileHistory(BaseModel):
    id = PrimaryKeyField(null=False, unique=True)
    file_hash = CharField(max_length=100, null=False, unique=True)
    file_name = CharField(max_length=500, null=False)
    file_path = CharField(max_length=1000, null=False)
    convert_status = BooleanField(default=False, null=False)
    conver_ddt = DateTimeField(default=None, null=True)
    copy_status = BooleanField(default=False, null=False)
    file_size = IntegerField(null=False)

    class Meta:
        database = db
        db_table = "file_history"
