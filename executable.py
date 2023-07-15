import time

def water_reminder():
    interval_minutes = 30  
    interval_seconds = interval_minutes * 60

    while True:
        
        print("Reminder: Drink water!")
        time.sleep(interval_seconds)

water_reminder()

with open("file.txt", "w+") as f:
    f.write("This is a computer virus!")