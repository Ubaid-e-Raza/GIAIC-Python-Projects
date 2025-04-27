import time
count_down = int(input("Enter time in seconds to start the countdown: "))
while count_down != 0:
    mins, sec = divmod(count_down, 60)
    timer = '{:02d}:{:02d}'.format(mins, sec)
    print(timer, end="\r")
    time.sleep(1)
    count_down -= 1
print('Timer Finished!')