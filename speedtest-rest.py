#!/usr/bin/env python

import StringIO
import csv
import decimal
import os
import subprocess

import requests
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

speedTestCliBin = os.getenv("SPEED_TEST_CLI_BIN")

response = subprocess.Popen(speedTestCliBin + ' --csv  --share', shell=True, stdout=subprocess.PIPE).stdout.read()
reader = csv.reader([response], dialect='excel')
for row in reader:
    row[6] = decimal.Decimal(row[6]) / 1000000
    row[7] = decimal.Decimal(row[7]) / 1000000
    payload = "{  \"server_id\": " + row[0] + ",  \"sponsor\": \"" + row[1] + "\",  \"server_name\": \"" + row[
        2] + "\",  \"timestamp\": \"" + row[3] + "\",  \"distance\": " + row[4] + ",  \"ping\": " + row[
                  5] + ",  \"download\": " + str(row[6]) + ",  \"upload\": " + str(row[7]) + ",  \"share\": \"" + row[
                  8] + "\",  \"ip_address\": \"" + row[9] + "\"}"
    r = requests.request("PUT", url, data=payload, headers=headers)
    print csv2string(row)
    # print r.status_code
    # print r.text
