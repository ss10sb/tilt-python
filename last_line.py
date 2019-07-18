import csv
from datetime import datetime

file = "/home/pi/log.csv"


def last():
    with open(file, "r") as f:
        offs = -100
        last = None
        rows = []
        while True:
            f.seek(offs, 2)
            lines = f.readlines()
            if len(lines) > 1:
                last = lines[-1]
                break
            offs *= 2
        if last:
            for row in csv.reader([last], delimiter=",", quoting=csv.QUOTE_NONE):
                dt = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
                rows.append({'color': row[5], 'date': dt, 'temp': row[2], 'gravity': "{0:.3f}".format(float(row[3]))})
        return rows
