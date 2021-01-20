import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Monitor the soup')
    parser.add_argument('reciever_address', metavar='r', help='Email address to send alerts to.')
    parser.add_argument('sender_address', metavar='s', help='Email address to send alerts from.')
    parser.add_argument('password', metavar='p', help='Password for sender_address.')
     parser.add_argument('devfile', metavar='d', help='Path to dev file where temp data can be read from.')
    parser.add_argument('-w', '--water_pin', type=int, default=-1, help='Pin used to monitor water level. Default is -1 meaning no water monitoring')
    parser.add_argument('-r', '--record_file', default='records.txt', help='Path to file to write temp records to')
    parser.add_argument('-m', '--measurement_interval', default=10, type=int, help='How long to pause between measurements in seconds.')
    parser.add_argument('-c', '--cooldown_time', default=300, type=int, help='How long to wait to send the next alert after sending an alert.')
    parser.add_argument('-i', '--ignore_all_errors', action='store_true', help='Flag, if set ignore all errors in main loop and just plow ahead. Default is false.')
    return parser.parse_args()