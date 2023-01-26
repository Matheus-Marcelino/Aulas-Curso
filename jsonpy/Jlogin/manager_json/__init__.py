from os import path
from json import dump, load, loads


class JsonManager():
    """Gerenciador de json"""

    def creat_json(self, filepath: str, writing: dict) -> None:
        """Cria uma arquivo json"""
        with open(filepath, "w+", encoding='utf-8') as file:
            dump(writing, file, indent=2, separators=(
                ',', ': '))  # escreve o arquivo json

    def read_json(self, filepath: str) -> (dict | bool):
        """Lê um arquivo json"""
        if path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as file:
                data = load(file)  # ler o arquivo json
            return data
        return False

    def update_json(self, filepath: str, data: dict) -> None:
        with open(filepath, 'w', encoding='utf-8') as file:
            dump(data, file, indent=2, separators=(',', ': '))
