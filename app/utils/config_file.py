import json
import os.path


def config_save(data):
    # 写入 JSON 文件
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def config_load():
    if not os.path.exists("data.json"):
        return {}
    # 读取 JSON 文件
    with open("data.json", "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
        return loaded_data


def config_set_bool(key: str, value: bool):
    data = config_load()
    data[key] = value
    config_save(data)


def config_get_bool(key: str):
    data = config_load()
    item = data.get(key)
    if item is None:
        return False

    return bool(item)


def config_set_list(key: str, value: list):
    data = config_load()
    data[key] = value
    config_save(data)


def config_get_list(key: str):
    data = config_load()
    item = data.get(key)
    if item is None:
        return []

    return list(item)
