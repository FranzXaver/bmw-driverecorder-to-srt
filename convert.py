#!/usr/bin/env python3
""" convert bmw driverecorder metadata to substitles """

import json
import os
from datetime import datetime

FPS = 30
FRAMETIME = 1.0/FPS
MYSRTNAME = "driverecorder.srt"

# try to set correct filename
for File in os.listdir("."):
    if File.endswith(".ts"):
        filename = os.path.splitext(File)
        MYSRTNAME = filename[0] + ".srt"

with open('Metadata.json',encoding=("us-ascii")) as jsonFile:
    data = json.load(jsonFile)
    with open(MYSRTNAME,'w',encoding=("us-ascii")) as subFile:
        for entry in data[0]['entries']:
            frame = entry['id']
            timeFrom = datetime.fromtimestamp((frame-1)*FRAMETIME+82800)\
                .strftime('%H:%M:%S,%f')[:-3]
            timeTo   = datetime.fromtimestamp(frame*FRAMETIME+82800)\
                .strftime('%H:%M:%S,%f')[:-3]
            subFile.write(f'{frame}\n')
            subFile.write(f'{timeFrom} --> {timeTo}\n')
            subFile.write(f'{entry["date"]} {entry["time"]}\n')
            subFile.write(f'{entry["velocity"]}km/h, '\
                          f'lat={entry["latitude"]}, '\
                          f'long={entry["longitude"]}\n\n')
