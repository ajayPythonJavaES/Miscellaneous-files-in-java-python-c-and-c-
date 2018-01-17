import time

def stopwatch():
    print("Stop watch")
    end_time = time.time() + (60)
    loop_var = 0
    while time.time() < end_time :
        loop_var = loop_var + 1
        print(loop_var)
        
