import json


def read_json(file_json):
    with open(file_json, encoding="utf8", mode="r") as file:
        obj = json.load(file)
    return obj


def write_json(file_name, obj):
    with open(file_name, mode="w", encoding="utf8") as file:
        json.dump(obj, file, ensure_ascii=False,indent=2)
