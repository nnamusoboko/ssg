import os
import shutil
import time
from pathlib import Path


def src_to_dest(src: Path, dest: Path):
    if os.path.exists(dest):
        try:
            shutil.rmtree(dest)
            time.sleep(0.1)
        except PermissionError:
            print("permision error")
            exit()

    if not os.path.exists(src):
        print("source dir doesnt exist")
        return

    if not os.path.exists(dest):
        os.mkdir(dest)

    if os.path.isdir(src):
        copy_files(src, dest)
    elif os.path.isfile(src):
        shutil.copy(src, os.path.join(dest, os.path.basename(src)))


def copy_files(src: Path, dest: Path):
    if not os.path.isdir(dest):
        os.mkdir(dest)

    for item in os.listdir(src):
        source_path = os.path.join(src, item)
        destination_path = os.path.join(dest, item)

        if os.path.isdir(source_path):
            copy_files(Path(source_path), Path(destination_path))

        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
