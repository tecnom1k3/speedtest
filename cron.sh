#!/usr/bin/env bash
/usr/bin/python /home/pi/speedtest/speedtest-rest.py >> /home/pi/speedtest/data/data.csv
/usr/local/bin/aws s3 sync /home/pi/speedtest/data s3://comcast-speedtest
