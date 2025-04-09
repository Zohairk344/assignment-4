import time

def Countdown(Time):
    while Time :
        Mins, Secs = divmod(Time, 60)
        Timer = "{:02d} : {:02d}".format(Mins, Secs)
        print(Timer, end="\r")
        time.sleep(1)
        Time -= 1
    print("Timer Completed")


if __name__ == "__main__" :
    Time = input("Enter Time in seconds: ")
    Countdown(int(Time))