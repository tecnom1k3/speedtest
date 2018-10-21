#!/usr/bin/env python
import datetime
import os
from os.path import join, dirname

import requests
from dotenv import load_dotenv
from requests import Timeout

dotEnvPath = join(dirname(__file__), '.env')
load_dotenv(dotenv_path=dotEnvPath)

awake = False
currentMinute = datetime.datetime.now().time().minute
tries = 8
count = 0

if (currentMinute + 1) % 20 == 0:
    print str(datetime.datetime.now()) + " - this is it!"
    url = os.getenv("WAKEUP_ENDPOINT")

    while count < tries:
        count = count + 1
        try:
            print str(datetime.datetime.now()) + " - trying request... " + str(count)
            r = requests.request("GET", url, timeout=5)
        except Timeout as error:
            print str(datetime.datetime.now()) + " - timeout!"
            continue
        else:
            print str(datetime.datetime.now()) + " - got response"
            try:
                response = r.json()
                if "status" in response:
                    status = response["status"]
                    if "wake" in status:
                        wake = status["wake"]
                        if wake == 1:
                            awake = True
                if awake:
                    print str(datetime.datetime.now()) + " - it's alive!"
                    break
            except ValueError:
                print str(datetime.datetime.now()) + " - response is not JSON"
                continue
else:
    print str(datetime.datetime.now()) + " - but mom..., 1 more minute please..."

if awake:
    print str(datetime.datetime.now()) + " - successfully awake!"
else:
    if count != 0:
        print str(datetime.datetime.now()) + " - not sure it is awake even though I tried..."
