from pathlib import Path

from tools.file_manager import file_status


def read_rom(file_path: str="sql/ROM.txt"):
    status = file_status(file_path)
    
    if not status[0]:
        raise ValueError("file_pathに有効なパスを入力してください")
    
    if not status[1]:
        raise ValueError("file_pathにファイルのパスを入力してください")
    
    if status[2] != ".txt":
        raise ValueError("ファイルの拡張子は、txtにしてください")
    