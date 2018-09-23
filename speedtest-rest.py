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

url = os.getenv("LOG_ENPOINT")
apiKey = os.getenv("APY_KEY")
headers = {'Content-Type': "application/json", 'x-api-key': apiKey}

speedtestCliBin = os.getenv("SPEED_TEST_CLI_BIN")

response = subprocess.Popen(speedtestCliBin + ' --csv  --share', shell=True, stdout=subprocess.PIPE).stdout.read()
reader = csv.reader([response], dialect='excel')
for row in reader:
	row[6] = decimal.Decimal(row[6])/1000000
	row[7] = decimal.Decimal(row[7])/1000000
	#payload = {"server_id": row[0],"sponsor": row[1],"server_name": row[2],"timestamp": row[3],"distance": row[4],"ping": row[5],"download": row[6],"upload": row[7],"share": row[8],"ip_address": row[9]}
	payload = "{\n  \"server_id\": 1782,\n  \"sponsor\": \"Comcast\",\n  \"server_name\": \"Seattle, WA\",\n  \"timestamp\": \"2018-09-21T05:10:01.930144Z\",\n  \"distance\": 15.042833314578802,\n  \"ping\": 25.612,\n  \"download\": 82.68025586921611,\n  \"upload\": 11.582651480139456,\n  \"share\": \"http://www.speedtest.net/result/7653589584.png\",\n  \"ip_address\": \"73.169.246.76\"\n}"
	r = requests.request("PUT", url, data=payload, headers=headers)
	print csv2string(row)
	print r.status_code
	print r.text
