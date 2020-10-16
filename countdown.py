import time
from playsound import playsound
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Blast Off!!!')
    playsound("G:/Program files/Python/alarm/alarm_dubstep.mp3")
t = input("Enter the time in seconds: ") 
countdown(int(t))