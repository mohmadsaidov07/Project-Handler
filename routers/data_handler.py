from fastapi import UploadFile
import json
import aiofiles
from typing import List, Dict

default_data_path = "test_data.json"
user_data_path = "user_data.json"

active_data = None
active_path = None


async def get_global_data(file: UploadFile | str | None = "") -> Dict[str, List]:
    global active_data
    global active_path

    if file is not None and not isinstance(file, str):
        file_data = await file.read()
        active_path = user_data_path
        async with aiofiles.open(active_path, "w") as f:
            active_data = await json.loads(file_data)
            await f.write(json.dumps(active_data))
        return active_data
    else:
        try:
            active_path = default_data_path
            async with aiofiles.open(active_path) as f:
                active_data = await json.loads(f)
                return active_data
        except FileNotFoundError:
            print("File not found: ", active_path)
            return {}


async def get_data():
    global active_data
    global active_path

    if active_data is None:
        try:
            active_path = default_data_path
            async with aiofiles.open(active_path) as f:
                active_data = await json.loads(f)
        except FileNotFoundError:
            print("File was not found", active_path)
    return active_data
