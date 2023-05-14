import os
import json
import datetime

if os.path.isdir("./output"):
    pass
else:
    os.mkdir("./output")


def list_to_json(list):
    current_date = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    os.mkdir(f"./output/{current_date}")

    with open(f"./output/{current_date}/likes.json", "w") as f:
        json.dump(list, f, indent=4)
