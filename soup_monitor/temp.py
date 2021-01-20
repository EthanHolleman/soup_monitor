import os
from datetime import datetime

def get_temp(dev_file):
    # https://iot4beginners.com/temperature-sensor-with-raspberry-pi-ds18b20/
    # Get temperature from DS18B20
    f = open(dev_file,"r")
    contents = f.readlines()
    f.close()
    index = contents[-1].find("t=")
    if index != -1 :
        temperature = contents[-1][index+2:]
        cels =float(temperature)/1000
        return cels

def write_temp(record_file, temp):
    if not os.path.exists(record_file):
        mode = 'w'
    else:
        mode = 'a'
    with open(record_file, mode) as handle:
        handle.write('{} {}\n'.format(datetime.now(), str(temp)))
    
    
    