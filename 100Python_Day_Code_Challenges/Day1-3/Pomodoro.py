"""
Walkthorugh:
- let the user set a duration.
- when its done notfiy him.
- make it countiously.
"""
import datetime, time

input_time = input("Enter Your Studying minutes: ")
print("Your Styduing time will be finished after {} Minutes".format(input_time))

duration = int(input_time) * 60
while True:
    print(datetime.timedelta(seconds=duration))
    duration -= 1
    if duration < 0:
        break
    time.sleep(1)
print("Time's Up")
