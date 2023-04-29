import re
import hashlib
from pathlib import Path


def create_path_hash(file_path: Path) -> str:
    str_file_path = str(file_path)
    hash_path = re.sub(r"(:|\\|\/)", "", str_file_path)
    hash_object = hashlib.md5(hash_path.encode())
    return hash_object.hexdigest()
