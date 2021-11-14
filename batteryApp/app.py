import time
import psutil
from pynotifier import Notification
import os


def battery(bat):
    '''Create notifications if battery<30 or if battery>90 
        and depending on the power_plugged status'''

    if bat.percent < 30 and bat.power_plugged == False:
        Notification(
            title='Plug the Charger',
            description=f'Battery  {bat.percent} %',
            icon_path=r'.\\icons\\low-battery-level.ico',
            duration=10,
            urgency='normal'
        ).send()

    elif bat.percent > 88 and bat.power_plugged == True:
        Notification(
            title='Unplug the Charger',
            description=f'Battery {bat.percent} %',
            icon_path=r'.\\icons\\battery.ico',
            duration=10,
            urgency='normal'
        ).send()


starttime = time.time()
while True:
    '''Call the battery function every 60 secs'''
    battery(psutil.sensors_battery())
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
    process = psutil.Process(os.getpid())
    print(process.memory_info().rss)
