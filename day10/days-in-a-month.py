# find the number of days in a given month after accounting for leap years
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

def is_leap(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False

def days_in_month(year, month):
	# normal non-leap days in the months
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  # if leap year add another day to february
  if is_leap(year) == True and month == 2:
	  # minus 1 from the month to account for zer0-indexing
	  # add 1 to the values that is stored at the index
	  return month_days[month - 1] + 1 # or return 29
  else:
	  # just get normal number of days for the month
	  return month_days[month - 1]

days = days_in_month(year, month)

print(days)
