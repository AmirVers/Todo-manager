import json
import uuid
from datetime import datetime


class Task:
    def __init__(self, description, completed=False, created_at=None, id=0):
        self.description = description
        self.completed = completed
        self.created_at = created_at or datetime.today()
        self.id = id or uuid.uuid4()

    def viaCompleted(self):
        self.completed = True

    def toJson(self):
        self._toReadable()
        json_dict = {
            "id": self.id,
            "desc": self.description,
            "completed": self.completed,
            "created": self.created_at,
        }
        return json_dict

    def _toReadable(self):
        if isinstance(self.created_at, datetime):
            self.created_at = self.created_at.strftime("%Y-%m-%d")
        if isinstance(self.id, uuid.UUID):
            self.id = self.id.hex

    @staticmethod
    def from_dict(data):
        created_at = datetime.strptime(data["created"], "%Y-%m-%d")
        return Task(data["desc"], data["completed"], created_at, data["id"])
