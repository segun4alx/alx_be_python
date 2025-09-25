# daily_reminder.py
# This script provides a customized reminder for a single task based on priority and time sensitivity.

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process based on priority using match case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unrecognized priority level."

# Check if the task is time-sensitive
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Display the customized reminder
print(f"Reminder: {reminder}")