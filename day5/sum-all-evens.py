# method 1
sum_of_evens = 0
for num in range(1,101):
	if num % 2 == 0:
		sum_of_evens += num
print(sum_of_evens)

# method 2, using a step value to skip over all odds numbers. more efficient than method 1
sum_of_evens = 0
for num in range(2, 101, 2):
	sum_of_evens += num
print(sum_of_evens)