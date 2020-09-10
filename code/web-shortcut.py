import webbrowser, datetime, logging
from time import sleep
from keyboard import read_key
try: from save import mapping
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

class LogHandler():
    def __init__(self):
        self.day = datetime.date.today().day
        self.month = datetime.date.today().month
        self.year = datetime.date.today().year
        self.minute = datetime.datetime.today().minute
        self.hour = datetime.datetime.today().hour

    def print_errors(self, filename, error):
        if self.hour > 12:
            self.hour -= 12
            filename.write("[{}-{}-{}]{}:{}PM: {}\n".format(self.day, self.month, self.year, self.hour, self.minute, error))
        elif self.hour == 12:
            filename.write("[{}-{}-{}]{}:{}PM: {}\n".format(self.day, self.month, self.year, self.hour, self.minute, error))
        elif self.hour == 0:
            filename.write("[{}-{}-{}]{}:{}AM: {}\n".format(self.day, self.month, self.year, self.hour, self.minute, error))
        else:
            filename.write("[{}-{}-{}]{}:{}AM: {}\n".format(self.day, self.month, self.year, self.hour, self.minute, error))

    def print_logs(self, key, url):
        if self.hour > 12:
            self.hour -= 12
            logging.info("[{}-{}-{}]{}:{}PM: [{}] => [{}]\n".format(self.day, self.month, self.year, self.hour, self.minute, key, url))
        elif self.hour == 12:
            logging.info("[{}-{}-{}]{}:{}PM: [{}] => [{}]\n".format(self.day, self.month, self.year, self.hour, self.minute, key, url))
        elif self.hour == 0:
            logging.info("[{}-{}-{}]{}:{}AM: [{}] => [{}]\n".format(self.day, self.month, self.year, self.hour, self.minute, key, url))
        else:
            logging.info("[{}-{}-{}]{}:{}AM: [{}] => [{}]\n".format(self.day, self.month, self.year, self.hour, self.minute, key, url))

logging.basicConfig(
    filename = r'..\key_logs.log',
    level = logging.INFO,
    format = '%(message)s'
)

if __name__ == "__main__":
    log_handler = LogHandler()
    while True:
        try:
            key = read_key()
            if key in mapping:
                if mapping[key] != "":
                    webbrowser.open(url=mapping[key])
                    log_handler.print_logs(
                        key = key,
                        url = mapping[key]
                    )
                    sleep(1)
                else:
                    continue
            else:
                continue
        except Exception as error:
            with open(r'..\traceback.txt', 'a+') as traceback:
                log_handler.print_errors(
                    filename = traceback,
                    error = error
                ); break