import json
from pathlib import Path

class Storage:
    def __init__(self, path: Path):
        self.path = path

    def save(self, engine) -> None:
        data = engine.to_dict()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load(self, engine) -> None:
        if not self.path.exists():
            return

        with self.path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        engine.from_dict(data)
