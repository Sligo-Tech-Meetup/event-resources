import os
from datetime import datetime

def create_event_folder(event_date):
    base_path = f"events/{event_date}"
    paths = [
        f"{base_path}/presentation",
        f"{base_path}/demo",
        f"{base_path}/assets"
    ]

    files = {
        f"{base_path}/index.md": "# Event Overview\n",
        f"{base_path}/speaker.md": "# Speaker Info\n",
        f"{base_path}/demo/README.md": "# Demo Instructions\n",
        f"{base_path}/metadata.yaml": f"date: {event_date}\ntitle: TBD\nspeaker: TBD\n",
    }

    for path in paths:
        os.makedirs(path, exist_ok=True)

    for filepath, content in files.items():
        with open(filepath, "w") as f:
            f.write(content)

    print(f"✅ Event folder structure for {event_date} created!")

if __name__ == "__main__":
    event_date = datetime.today().strftime("%Y-%m")
    create_event_folder(event_date)
