import webbrowser, datetime
from time import sleep
from keyboard import read_key
try:
    from save import mapping
except ModuleNotFoundError:
    with open('save.py', 'w') as save:
        save.write("""
mapping = {
    "f1": "https://www.google.com",
    "f2": "https://www.youtube.com",
    "f3": "https://www.discord.com",
    "f4": "https://www.twitch.tv",
    "f5": "https://www.github.com",
    "f6": "",
    "f7": "",
    "f8": "",
    "f9": "",
    "f10": "",
    "f11": "",
    "f12": "",
    "home": "",
    "end": "",
    "delete": "",
    "insert": "",
    "pause": ""
}
        """)
        exit()

if __name__ == "__main__":
    keys = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12", "home", "end", "delete", "insert", "pause"]
    while True:
        try:
            key = read_key()
            if key in keys:
                if mapping[key] != "":
                    webbrowser.open(url=mapping[key])
                    sleep(1)
                else:
                    continue
            else:
                continue
        except Exception as error:
            with open(r'..\traceback.txt', 'a+') as traceback:
                day = datetime.date.today().day
                month = datetime.date.today().month
                year = datetime.date.today().year
                minute = datetime.datetime.today().minute
                hour = datetime.datetime.today().hour
                if hour > 12:
                    hour -= 12
                    traceback.write("[{}-{}-{}]{}:{}PM: {}\n".format(day, month, year, hour, minute, error))
                elif hour == 12:
                    traceback.write("[{}-{}-{}]{}:{}PM: {}\n".format(day, month, year, hour, minute, error))
                elif hour == 0:
                    traceback.write("[{}-{}-{}]{}:{}AM: {}\n".format(day, month, year, hour, minute, error))
                else:
                    traceback.write("[{}-{}-{}]{}:{}AM: {}\n".format(day, month, year, hour, minute, error))
                break