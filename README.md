# Python-Alarm-Clock

![Python Alarm Clock Logo](logo.svg)

---
## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Setting Multiple Alarms](#setting-multiple-alarms)
- [Code Explanation](#code-explanation)
  - [Imports and Initialization](#imports-and-initialization)
  - [Setting Multiple Alarms](#setting-multiple-alarms-function)
  - [Main Program Execution](#main-program-execution)
- [Customization](#customization)
- [Known Issues](#known-issues)
- [Contributing](#contributing)

---
## Introduction

Welcome to the Python Alarm Clock project! This simple yet functional alarm clock allows users to set multiple alarms using a friendly command-line interface (CLI). The script notifies users when the alarm time is reached, and it includes visual enhancements using color to improve readability.

This project is perfect for learning basic Python concepts such as time handling, loops, functions, and external libraries like `colorama`.

---
## Features

- **Multiple Alarms**: Set as many alarms as you need.
- **12-Hour Format**: Input alarm times in the user-friendly 12-hour format with AM/PM.
- **Real-Time Monitoring**: Continuously displays the current time while waiting for alarms to trigger.
- **Colorful Output**: Enhanced visual output using the `colorama` module for a more appealing interface.
- **Automatic Exit**: The script automatically exits once all alarms have triggered.

## Requirements

To run this project, you'll need:
- Python 3.6 or higher
- The `colorama` module (for colored output in the terminal)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mdriyadkhan585/Python-Alarm-Clock
   cd Python-Alarm-Clock
   ```

2. **Install Dependencies:**
   You can install the required `colorama` module using pip:
   ```bash
   pip install colorama
   ```

3. **Run the Script:**
   ```bash
   python alarm_clock.py
   ```

## Usage

### Setting Multiple Alarms

1. **Run the Script**: Start the script using your Python interpreter.
2. **Input Alarm Times**: 
   - Enter the alarm time(s) in `HH:MM AM/PM` format when prompted.
   - Type `'done'` to finish setting alarms.
3. **Wait**: The script will display the current time and notify you when each alarm goes off.
4. **Exit**: The script automatically exits after all alarms have been triggered.

### Example Usage:
```bash
========================================
        Python Alarm Clock
========================================

Enter the time to set an alarm (HH:MM AM/PM) or type 'done' to finish: 07:30 AM

Enter the time to set an alarm (HH:MM AM/PM) or type 'done' to finish: 12:00 PM

Enter the time to set an alarm (HH:MM AM/PM) or type 'done' to finish: done

========================================
Alarms set for the following times:
- 07:30 AM
- 12:00 PM
========================================

Current time: 07:29 AM | Waiting for the next alarm...
```

## Code Explanation

### Imports and Initialization

```python
import time
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)
```
- **time**: Provides functions to handle time-related tasks.
- **datetime**: Provides functions to handle date and time.
- **colorama**: Enables colored text output in the terminal.

### Setting Multiple Alarms Function

```python
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
```
- **set_alarms**: This function manages all the alarms the user has set. It continuously checks the current time against the set alarms and notifies the user when an alarm is triggered.

### Main Program Execution

```python
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
```
- **get_alarm_times**: This function prompts the user to enter alarm times. It checks the format and stores valid alarm times in a list.
- **Main Execution**: Combines the `get_alarm_times` and `set_alarms` functions to create a fully functioning alarm clock.

## Customization

- **Alarm Sound**: You can add a sound alert when the alarm goes off by using the `playsound` module or similar.
- **Time Interval**: Modify the `time.sleep(10)` line to change how often the script checks the current time (e.g., every 5 seconds or every minute).
- **24-Hour Format**: Adjust the time parsing and display format if you prefer the 24-hour time format.

## Known Issues

- **Exact Minute Trigger**: The alarm only triggers at the exact minute set. It does not account for seconds, so if you set the alarm for `07:30 AM`, it will trigger only if the script is running at `07:30:00 AM`.
- **Terminal Compatibility**: The colored output works best in terminals that support ANSI escape sequences. Some environments might not display colors correctly.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue on GitHub if you have any ideas for improvements or bug fixes.

---
