# Test if an electrical connection between
# wires are made. Will be used to detect if water
# level falls below line.
# Wire pin to GPIO and other to 3 volt pin
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

def setup_pin_as_read(pin_num):
    GPIO.setup(pin_num, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def read_state(pin_num=10):
    # True is closed false is open.
    if GPIO.input(pin_num) == GPIO.HIGH:
        return True
    else:
        return False
    
    