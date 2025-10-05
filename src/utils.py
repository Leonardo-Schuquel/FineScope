from pathlib import Path
import json
import sys

# Function to determine the base folder, compatible with PyInstaller
def get_base_path():
    if getattr(sys, 'frozen', False):
        # Executable by PyInstaller
        return Path(sys.executable).parent
    else:
        # Normal execution
        return Path(__file__).parent

FOOLDER_ROOT = get_base_path()

foolder_data = FOOLDER_ROOT / 'Data'
path_data = foolder_data / 'data.json'

# Create folder and file if they do not exist
foolder_data.mkdir(exist_ok=True)
path_data.touch(exist_ok=True)

# Initialize the JSON to empty if it is empty
if path_data.stat().st_size == 0:
    with path_data.open('w', encoding='utf-8') as f:
        json.dump([], f, ensure_ascii=False, indent=4)

# Loading json
def loadJson():
    try:
        with open(path_data, 'r', encoding='utf-8') as file:
            release = json.load(file)
            if isinstance(release, dict):
                return release
            return {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Creation of id
def create_id():
    release = loadJson()
    max_id = 0
    for month_data in release.values():
        for entry in month_data:
            if 'id' in entry and isinstance(entry['id'], int):
                max_id = max(max_id, entry['id'])
    return max_id + 1

# Records
def balance(event: str):
    releses = loadJson()
    balance = 0

    for month, launch in releses.items():
        for launches in launch:
            if launches['event'] == event:
                balance += launches['value']

    return f"{balance:.2f}"

def total_balance():
    positive = float(balance('Entrada'))
    negative = float(balance('Saida'))

    total = positive - negative

    return f"{total:.2f}"