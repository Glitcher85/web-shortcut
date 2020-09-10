import importlib, webbrowser, datetime, logging, script
from time import sleep
from keyboard import read_key
try: import save
except ModuleNotFoundError:
    with open('save.py', 'w') as save:
        save.write(script.data)
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
        importlib.reload(save)
        try:
            key = read_key()
            if key in save.mapping:
                if save.mapping[key] != "":
                    webbrowser.open(url=save.mapping[key])
                    log_handler.print_logs(
                        key = key,
                        url = save.mapping[key]
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