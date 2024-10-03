import warnings

from pathlib import Path

def check_file_size(file: Path) -> None:
    if file.stat().st_size > 1024 ** 3:
        warnings.warn("File size exceed 1 GB, if your machine cannot process this successfully, you may require more memory."