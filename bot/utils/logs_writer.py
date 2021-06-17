import logging
from os import path, listdir, remove
import time
from math import floor


class LogsWriterHandler(logging.Handler):
    def emit(self, record):
        if self.log_date_file + 86400 < time.time():
            self.log_date_file = floor(time.time())
        print()
        if path.exists(f"logs/{self.log_date_file}.log"):
            f = open(f"logs/{self.log_date_file}.log", "a", encoding="utf-8")
            f.write(f"{record.getMessage()}\n")
        else:
            f = open(f"logs/{self.log_date_file}.log", "w", encoding="utf-8")
            f.write(f"{record.getMessage()}\n")
        f.close()
        for f in [i.split(".")[0] for i in listdir("logs")]:
            if int(f) + 604800 < floor(time.time()):
                remove("logs/"+f+".log")
                



        


