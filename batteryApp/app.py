import datetime 
import time 
import psutil
from pynotifier import Notification
  
visit = 0

def battery(bat,visit):
    if bat.percent < 50 and bat.power_plugged == False:
        if visit%3 == 0:
            Notification(
                title='Plug the Charger',
                description=f'Battery % {bat.percent}',
                icon_path= 'D:\\Projects\\Battery Notification\\batteryApp\\low-battery-level.ico', 
                duration=10,                                  
                urgency='normal'
            ).send()
        visit+=1
        return visit

    elif bat.percent > 90 and bat.power_plugged == True:
        if visit%3 == 0:
            Notification(
                title='Unplug the Charger',
                description=f'Battery % {bat.percent}',
                icon_path= 'D:\\Projects\\Battery Notification\\batteryApp\\battery.ico', # On Windows .ico is required, on Linux - .png
                duration=10,                                   # Duration in seconds
                urgency='normal'
            ).send()
        visit+=1
        return visit
    else:
        return visit
   
starttime = time.time()
while True:
    visit = battery(psutil.sensors_battery(), visit)
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
