import json
import datetime

defaults = {
    "lat": -37,
    "lon": 145,
    "elev": 100,
    "date": str(datetime.date.today()),
    "time": str(datetime.datetime.now().time()),
    "timezone": 21,
    "auto_update": True,
    "auto_update_before_override": False,
    "use_custom_time": False,
    "antenna_temp": 9.1 * 10 ** 4,
}
def load():
    try:
        open("savedata.json", "r")
    except FileNotFoundError:
        return defaults

    else:
        with open("savedata.json", "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                write(defaults)
                return defaults



def write(data):
    with open("savedata.json", "w") as f:
        print(json.dumps(data, indent=4), file=f)
