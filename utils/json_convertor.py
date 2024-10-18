import json


def load_json(file_path):
    try:
        with open(f"json_db/{file_path}", 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"Файл по пути {file_path} не найден.")
        return None
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON.")
        return None