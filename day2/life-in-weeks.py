# Life remaining in days, weeks, years
# Assumes you will live til age 90
age = int(input("What is your current age?"))
yearsleft = 90 - age
days = round( yearsleft * 365)
weeks = round( yearsleft * 52)
months = round( yearsleft * 12)
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
