from pathlib import Path


def check_free_file(file_path: Path):
    if not file_path.exists():
        raise FileNotFoundError
    try:
        file_path.rename(file_path)
    except PermissionError:
        return False
    else:
        return True
