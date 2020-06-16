import os
from datetime import datetime

class make_csv:

    def __init__(self, value):
        self.value = value
        print(value)

    def make_dir(self, path):
        if not os.path.isdir(path):
            os.makedirs(path)

    def write_file(self, file):
        f = open(file, "w", encoding="UTF8")
        f.write(f"{self.value}\n")
        f.close()

    def save(self):
        dir_month = datetime.today().strftime("%Y-%m")
        dir_day = datetime.today().strftime("%d")
        file_name = datetime.today().strftime("%H%M")

        path = f"/project/stock/data/{dir_month}/{dir_day}"
        self.make_dir(path)
        print(path)

        file = f"{path}/{file_name}.csv"
        self.write_file(file)
        print(file)
