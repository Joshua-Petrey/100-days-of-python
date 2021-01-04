# if a number appears in file 1 and file 2 add it to the list 

with open('./file1.py') as f1:
    file1 = f1.readlines()

with open('file2.py') as f2:
     file2 = f2.readlines()

# if the num in file1 is also in file2 add it to the list
numbers_in_both = [int(number.strip()) for number in file1 if number in file2]

print(numbers_in_both)