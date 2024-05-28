import time
t = time.strftime('%H:%M:%S')
print(t)

name = input("Enter Your Name: ")
hour = int(time.strftime('%H'))

if(hour >= 0 and hour < 12):
    print(f"Good Morning {name}")
elif(hour >= 12 and hour < 18):
    print(f"Good Evening {name}")
if(hour >= 18 and hour < 0):
    print(f"Good Evening {name}")
