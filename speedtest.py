#!/usr/bin/env python

import StringIO
import csv
import decimal
import subprocess


def csv2string(data):
    si = StringIO.StringIO()
    cw = csv.writer(si)
    cw.writerow(data)
    return si.getvalue().strip('\r\n')


response = subprocess.Popen('/home/pi/speedtest/bin/speedtest-cli --csv  --share', shell=True,
                            stdout=subprocess.PIPE).stdout.read()
reader = csv.reader([response], dialect='excel')
for row in reader:
    row[6] = decimal.Decimal(row[6]) / 1000000
    row[7] = decimal.Decimal(row[7]) / 1000000
    print csv2string(row)
