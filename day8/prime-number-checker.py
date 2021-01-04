# Check if a number is Prime
num = int(input("Number to check\n"))

def prime_checker(number):
    if number > 1:
        for x in range(2, number):
            if (number % x) == 0:
                print(f"{number} is NOT a prime number")
                break
        else:
            print(f"{number} Is a Prime Number")
    else:
        print(f"{number} Is NOT a Prime Number")


prime_checker(num)
