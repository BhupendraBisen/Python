import time
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
hour = int(input("Enter hour:"))
print(hour)

if(hour>=0 and hour<12):
    print("good morning sir!")
elif(hour>=12 and hour<17):
    print("good afternoon sir!")
if (hour>=17 and hour<=23):
    print("good night sir!")

