from soup_monitor.email import *
from soup_monitor.button import *
from soup_monitor.temp import *
from soup_monitor.args import *
import time

# 8479225317@txt.att.net'
# %Run run.py 8479225317@txt.att.net ethansbot2@gmail.com 782Judson

def main():
    '''Main loop, coordinates measurements, recording and
    sending alerts.
    '''
    # Set everything up here
    args = get_args()
    email = connect(args.sender_address, sender_password=args.password)
    if args.water_pin > 0:
        setup_pin_as_read(args.water_pin)
    cooldown = time.time()
    
    # Enter loop until process is killed or error
    iter_counter = 0
    while True:
        print('Starting measurement iteration {}'.format(iter_counter))
        try:
            if args.water_pin > 0:
                water_state = read_state(args.water_pin)
                print(water_state)
                if water_state == False:
                    if abs(cooldown - time.time()) > args.cooldown_time:
                        message = 'Pot is low on water!'
                        send_message(email,
                                     message,
                                     args.sender_address,
                                     args.reciever_address)
                        cooldown = time.time()
            
            cur_temp = get_temp(args.dev_file)
            if cur_temp < 90:
                if abs(cooldown - time.time()) > args.cooldown_time:
                    message = 'Pot is not boiling!'
                    send_message(email,
                                 message,
                                 args.sender_address,
                                 args.reciever_address)
                    cooldown = time.time()
            
            write_temp(args.record_file, cur_temp)
            time.sleep(args.measurement_interval)
            iter_counter += 1
        except Exception as e:
            if args.ignore_all_errors == True:
                continue
            else:
                message = 'Encountered error program stopped! {}'.format(e)
                send_message(email,
                             message,
                             args.sender_address,
                             args.reciever_address)
                raise e
            

if __name__ == '__main__':
    main()

