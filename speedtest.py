#!/usr/bin/env python

import csv
import decimal
import subprocess

with subprocess.Popen('/home/pi/speedtest/bin/speedtest-cli --csv  --share', shell=True, stdout=subprocess.PIPE).stdout.read() as response:
	reader = csv.reader([response], dialect='excel')
	for row in reader:
		print '"{}","{}","{}","{}","{}","{}","{}","{}","{}","{}"'.format(row[0], row[1], row[2], row[3], row[4], row[5], decimal.Decimal(row[6])/1000000, decimal.Decimal(row[7])/1000000, row[8], row[9])
