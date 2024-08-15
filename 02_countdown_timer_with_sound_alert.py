# Countdown timer with sound alert
import time
import winsound

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Time Up!')
    winsound.Beep(2500, 1000)  # 2500 Hz frequency for 1 second

# input time in seconds
t = input("Enter the time in seconds: ")

countdown(int(t))
