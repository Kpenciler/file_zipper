from typing import List, Union
import os
import shutil
import zipfile
import pyminizip

import secrets
import string

def zip_files(src: Union[str, List[str]], dst: str, password: str) -> bool:
    try:
        # 型のチェック
        if isinstance(src, str):
            src_list = [src]
        elif isinstance(src, list) and all(isinstance(src_i, str) for src_i in src):
            src_list = src
        else:
            assert False, "Invalid src: [str, List[str]]"
        pyminizip.compress_multiple([os.path.basename(src_i) for src_i in src_list],
                                    [os.path.dirname(src_i) for src_i in src_list],
                                    dst, password, 4)
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False

def generate_password(length: int = 8) -> str:
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password
