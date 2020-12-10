# leap year occurs on every year cleanly divisible by 4
# except on years cleanly divisible by 100
# unles those years are cleany diviible by 400

year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
