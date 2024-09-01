import time
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def set_alarms(alarm_times):
    print(f"\n{Fore.CYAN + '='*40}")
    print(Fore.CYAN + "Alarms set for the following times:")
    for alarm_time in alarm_times:
        print(Fore.GREEN + f"- {alarm_time.strftime('%I:%M %p')}")
    print(Fore.CYAN + '='*40 + "\n")

    while True:
        # Get the current time
        now = datetime.now().time()

        # Check if the current time matches any of the alarm times
        for alarm_time in alarm_times:
            if now.hour == alarm_time.hour and now.minute == alarm_time.minute:
                print(f"\n\n{Fore.YELLOW + '*'*40}")
                print(Fore.YELLOW + f"**  Wake up! It's {alarm_time.strftime('%I:%M %p')}  **")
                print(Fore.YELLOW + '*'*40 + "\n")
                alarm_times.remove(alarm_time)  # Remove the triggered alarm from the list

        # If no more alarms are left, break the loop
        if not alarm_times:
            print(Fore.CYAN + "All alarms have triggered. Exiting alarm clock.")
            break

        # Show the current time to the user
        print(f"\r{Fore.MAGENTA}Current time: {now.strftime('%I:%M %p')} | Waiting for the next alarm...", end="")
        
        # Wait for 10 seconds before checking again
        time.sleep(10)

# Input multiple alarm times in HH:MM AM/PM format
def get_alarm_times():
    alarm_times = []
    print(Fore.CYAN + '='*40)
    print(Fore.CYAN + "        Python Alarm Clock")
    print(Fore.CYAN + '='*40)
    
    while True:
        alarm_time_str = input(Fore.YELLOW + "\nEnter the time to set an alarm (HH:MM AM/PM) or type 'done' to finish: ")
        if alarm_time_str.lower() == 'done':
            break
        try:
            alarm_time = datetime.strptime(alarm_time_str, "%I:%M %p").time()
            alarm_times.append(alarm_time)
        except ValueError:
            print(Fore.RED + "Invalid time format. Please use HH:MM AM/PM format.")

    return alarm_times

# Get the list of alarm times from the user
alarm_times = get_alarm_times()

# Set the alarms if any are provided
if alarm_times:
    set_alarms(alarm_times)
else:
    print(Fore.RED + "No alarms were set.")
