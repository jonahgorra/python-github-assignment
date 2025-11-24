print("Welcome to my Python program!")
hours_input = input("How many hours did you study today? ")
daily_hours = float(hours_input)
weekly_hours = daily_hours * 7
print(f"You are on track to study approximately {weekly_hours} hours this week.")
try:
    daily_hours = float(hours_input)
    weekly_hours = daily_hours * 7
    print(f"You are on track to study approximately {weekly_hours} hours this week.")
except ValueError:
    print("Please enter a valid number.")
    exit()
