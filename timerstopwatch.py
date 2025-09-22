import time
import os
import sys

print("Timer / Stopwatch")
while True:
    option = input("Do you want the timer or stopwatch? T/S: ")
    if option.lower() in ["t", "s"]:
        option = option.upper()
        break
    else:
        print("Type in T or S \n")

def get_number(type):
    while True:
        number = input(f"How many {type} do you want on the timer?: ")
        if number.isdigit():
            number = int(number)
            if (type == "hours" and number < 25) or (type != "hours" and number < 60):
                return number
        if type == "hours":
            print("The number of hours must be 24 or less\n")
        else:
            print(f"The number of {type} must be less than 60\n")

def timer():
    hours = int(get_number("hours"))
    minutes = int(get_number("minutes"))
    seconds = int(get_number("seconds"))
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        additive_h = "0" if len(str(hours)) < 2 else ''
        additive_m = "0" if len(str(minutes)) < 2 else ''
        additive_s = "0" if len(str(seconds)) < 2 else ''
        print(f"{additive_h}{hours}:{additive_m}{minutes}:{additive_s}{seconds}")
        time.sleep(1)
        if seconds != 0:
            seconds = seconds - 1
        elif seconds == 0:
            if minutes != 0:
                minutes = minutes - 1
                seconds = 59
            elif minutes == 0:
                if hours != 0:
                    minutes = 59
                    seconds = 59
                    hours = hours - 1
                elif hours == 0:
                    while True:
                        os.system("say beep")
                        print("Time's Up!")
                    break

def stopwatch():
    hours = 0
    minutes = 0
    seconds = 0
    while True:
        additive_h = "0" if len(str(hours)) < 2 else ''
        additive_m = "0" if len(str(minutes)) < 2 else ''
        additive_s = "0" if len(str(seconds)) < 2 else ''
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{additive_h}{hours}:{additive_m}{minutes}:{additive_s}{seconds}")
        time.sleep(1)
        if seconds != 59:
            seconds = seconds + 1
        elif seconds == 59:
            seconds = 0
            if minutes != 59:
                minutes = minutes + 1
            elif minutes == 59:
                if hours != 24:
                    hours = hours + 1
                elif hours == 24:
                    print("Limit Reached!")
                    break

if option == "T":
    timer()
else:
    stopwatch()
