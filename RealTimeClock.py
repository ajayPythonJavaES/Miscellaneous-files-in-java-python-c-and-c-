import datetime
import time

date = datetime.datetime.now().date()

def runRTC():
    print("Current date and time: ", datetime.datetime.now())
    timeInSec = 1
    takeInput = input("Please enter the end time(hh:mm:ss), 24-hour format: ")
    hour,minutes,sec = takeInput.split(":")
    hour = int(hour)
    minutes = int(minutes)
    sec = int(sec)
    currHour = datetime.datetime.now().hour
    currMin = datetime.datetime.now().minute
    currSec = datetime.datetime.now().second
    if(hour < currHour):
        print("Entered hour is less than the current hour")
    elif(hour > currHour and minutes > currMin and sec > currSec):
        timeInSec = timeInSec * (hour - currHour) * 3600 * (minutes - currMin) * 60 * (sec - currSec)
    elif(minutes < currMin and hour == currHour and (sec == 0 or sec == currSec)):
        print("Entered minute is less than the current minute")
    elif(minutes > currMin and hour == currHour and (sec == 0 or sec == currSec)):
        timeInSec = timeInSec * (minutes - currMin) * 60
    elif(minutes < currMin and hour > currHour and (sec == 0 or sec == currSec)):
        timeInSec = timeInSec * ((60-minutes) + currMin) * 60
    elif(sec < currSec and hour == currHour and minutes == currMin):
        print("Entered second is less than the current second")
    elif(sec > currSec and hour == currHour and minutes == currMin):
        timeInSec = timeInSec * (sec - currSec)
    elif(sec < currSec and hour == currHour and minutes > currMin):
        timeInSec = timeInSec * ((((minutes-currMin)*60 + sec)) - currSec)
    elif(sec > currSec and hour == currHour and minutes > currMin):
        timeInSec = timeInSec * (minutes - currMin)*60 * (sec - currSec)

    if(timeInSec > 1):
            runLoop(timeInSec)        


def runLoop(secs):
    dispStr = input("Please enter a string:")
    end_time = time.time() + (secs)
    #print(time.time())
    #print(end_time)
    loop_var = 0
    while time.time() < end_time :
        loop_var = loop_var + 1
        if(loop_var%217 == 0):
            print(dispStr)
    exitStr = input("Press any key to exit")    
    return


def takeInputTime():
    take_time = input("Please enter time in the format(hh:mm:ss): ")
    hour,minutes,sec = take_time.split(":")
    timeInSec = 1
    if(int(hour) != 0):
        timeInSec = timeInSec * int(hour) * 3600
    if(int(minutes) != 0):
        timeInSec = timeInSec * int(minutes) * 60
    if(int(sec) > 0):
        timeInSec = timeInSec * int(sec)
    runLoop(timeInSec)            
                    
                
        
runRTC()
