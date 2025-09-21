#import os
#import winsound
#import sys
from datetime import datetime
from zoneinfo import ZoneInfo

print("To-Do List\n")
commands = ['help','view list', 'edit list', 'set reminders','reboot']
to_dolist = []
print(f'Commands: {commands[0]}, {commands[1]}, {commands[2]}, {commands[3]}, {commands[4]}')

def execute_command():
    # START
    print("Command Executed!")

def gettime():
    # Use ZoneInfo for accurate, system-based timezones
    central_timezone = ZoneInfo("America/Chicago")
    now_central_time = datetime.now(central_timezone)
    current_time = now_central_time.strftime('%H:%M:%S')
    return current_time
    
def add_to_list():
    # REMEMBER, TO_DOLIST IS ALREADY INSTANTIATED
    # START
    print("Added to list!")
    
def main():
    # START
    command = input("Enter your command: ")
    
if __name__ == "__main__":
    main()