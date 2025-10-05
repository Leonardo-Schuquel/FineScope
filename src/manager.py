from utils import path_data, loadJson, create_id
from datetime import datetime
import json

class Management:
    def __init__(self, event: str, value: float, title: str,
                 description: str | None = None) -> None:
        self.event = event
        self.value = value
        self.title = title
        self.description = description

    def collecting(self):
        """Capture of data to be filled in by the user"""
        id = create_id()
        date_time = datetime.now().strftime('%d/%m/%Y %H:%M')

        data = {
            'id': id,
            'event': self.event,
            'title': self.title,
            'value': self.value,
            'description': self.description,
            'date_time': date_time,
        }

        return data

    def save(self, data):
        """Save entries"""
        current_month = datetime.now().strftime('%m/%Y')

        release = loadJson()

        if current_month not in release:
            release[current_month] = []

        release[current_month].append(data)

        with open(path_data, 'w', encoding='utf-8') as file:
            json.dump(release, file, indent=4, ensure_ascii=False)

    @staticmethod
    def getCurrentMonth():
        """Get the current month"""
        current_month = datetime.now().strftime("%m/%Y")
        data = loadJson()
        return data.get(current_month, [])
    
    def edit_release(self, _id):
        """Edits a specific release"""
        release = loadJson()
        current_month = datetime.now().strftime('%m/%Y')

        for i, launch in enumerate(release[current_month]):
            if launch['id'] == _id:
                release[current_month][i] = {
                    'id': _id,
                    'event': self.event,
                    'title': self.title,
                    'value': self.value,
                    'description': self.description,
                    'date_time': launch.get('date_time')
                }
                
                with open(path_data, 'w', encoding='utf-8') as file:
                    json.dump(release, file, indent=4, ensure_ascii=False)

    @staticmethod
    def exclude_release(_id):
        release = loadJson()
        current_month = datetime.now().strftime('%m/%Y')

        for i, launch in enumerate(release[current_month]):
            if launch['id'] == _id:
                release[current_month].pop(i)
                
                with open(path_data, 'w', encoding='utf-8') as file:
                    json.dump(release, file, indent=4, ensure_ascii=False)
                return True
            return False

    @staticmethod
    def delRelease(release_id: str):
        release = loadJson()
        found = False

        for month, launches in release.items():
            for i, launch in enumerate(launches):
                if launch["id"] == release_id:
                    launches.pop(i)
                    found = True
                    break
            if found:
                break
        
        if found:
            with open(path_data, 'w', encoding='utf-8') as file:
                json.dump(release, file, indent=4, ensure_ascii=False)
            return True
        
        return False