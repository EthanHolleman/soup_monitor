# soup_monitor
Small program to monitor soup temperature and broth level using Raspberry Pi.

```
usage: run.py [-h] [-w WATER_PIN] [-r RECORD_FILE] [-m MEASUREMENT_INTERVAL]
              [-c COOLDOWN_TIME] [-i]
              r s p d

Monitor the soup

positional arguments:
  r                     Email address to send alerts to.
  s                     Email address to send alerts from.
  p                     Password for sender_address.
  d                     Path to dev file where temp data can be read from.

optional arguments:
  -h, --help            show this help message and exit
  -w WATER_PIN, --water_pin WATER_PIN
                        Pin used to monitor water level. Default is -1 meaning
                        no water monitoring
  -r RECORD_FILE, --record_file RECORD_FILE
                        Path to file to write temp records to
  -m MEASUREMENT_INTERVAL, --measurement_interval MEASUREMENT_INTERVAL
                        How long to pause between measurements in seconds.
  -c COOLDOWN_TIME, --cooldown_time COOLDOWN_TIME
                        How long to wait to send the next alert after sending
                        an alert.
  -i, --ignore_all_errors
                        Flag, if set ignore all errors in main loop and just
                        plow ahead. Default is false.
```
