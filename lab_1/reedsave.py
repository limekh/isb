import json


def read_json(dir: str) -> dict:
    """
    Reads JSON file
    :param dir: Path to the JSON file
    :return: JSON file
    """
    try:
        with open(dir, mode='r', encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError as e:
        print(f"File does not exist: {e}")
    except PermissionError as e:
        print(f"Can't access this file: {e}")
    except Exception as e:
        print(f"Something wrong:{e}")


def get_text(dir: str) -> str:
    """
    Opens text file
    :param dir: path to the .txt file
    :return: .txt file as a string
    """
    try:
        with open(dir, mode='r', encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError as e:
        print(f"File does not exist: {e}")


def save_text(dir: str, text: str) -> None:
    """
    Saves string to .txt file
    :param dir: path to save .txt file
    :param text: string to save
    :return: None
    """

    try:
        with open(dir, mode='w', encoding="utf-8") as file:
            file.write(text)
    except Exception as e:
        print(f"Something went wrong: {e}")


def save_json(dir: str, data: dict) -> None:
    """
    Saves dictionary as json file
    :param dir: path to save .json file
    :param data: dictionary to save
    :return: None
    """
    try:
        with open(dir, mode='w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)
    except FileNotFoundError as e:
        print(f"File does not exist: {e}")
    except PermissionError as e:
        print(f"Can't access this file: {e}")
    except Exception as e:
        print(f"Something went wrong: {e}")
