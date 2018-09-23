#!/usr/bin/env python

import csv
import decimal
import subprocess
import StringIO
import requests
import os

from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

def csv2string(data):
    si = StringIO.StringIO()
    cw = csv.writer(si)
    cw.writerow(data)
    return si.getvalue().strip('\r\n')

endpoint = os.getenv("LOG_ENPOINT")

response = subprocess.Popen('/home/pi/speedtest/bin/speedtest-cli --csv  --share', shell=True, stdout=subprocess.PIPE).stdout.read()
reader = csv.reader([response], dialect='excel')
for row in reader:
	row[6] = decimal.Decimal(row[6])/1000000
	row[7] = decimal.Decimal(row[7])/1000000
        payload = {"server_id": row[0],"sponsor": row[1],"server_name": row[2],"timestamp": row[3],"distance": row[4],"ping": row[5],"download": row[6],"upload": row[7],"share": row[8],"ip_address": row[9]}
        r = requests.put(endpoint, data=payload)
	print csv2string(row)
