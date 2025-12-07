import datetime # Handles UTC time
import time # Handles pausing mechanisms

def setAlarm():
    while True:
        try:
            alarmHr = int(input("Enter hour for alarm (0-23): "))
            alarmMin = int(input("Enter minute for alarm (0-59): "))
            if 0 <= alarmHr <= 23 and 0 <= alarmMin <= 59:
                break
            else:
                print("Invalid time! Please enter valid hour (0-23) and minute (0-59)")
        except ValueError:
            print("Invalid input! Please enter a number")
    
    print(f"Alarm set for {alarmHr:02d}:{alarmMin:02d}")
    

    while True:
        now = datetime.datetime.now()
        if now.hour == alarmHr and now.minute == alarmMin:
            print("TIME TO WAKE UP")
            break
        time.sleep(1)

if __name__ == "__main__":
    setAlarm()


