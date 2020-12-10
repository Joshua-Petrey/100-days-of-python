name1 = input("What is your name?").lower()
name2 = input("What is their name?").lower()

trucol = 0
luvcol = 0
for letter in "true":
    if name1.count(letter) >= 1:
        trucol += name1.count(letter)
    if name2.count(letter) >= 1:
        trucol += name2.count(letter)

for letter in "love":
    if name1.count(letter) >= 1:
        luvcol += name1.count(letter)
    if name2.count(letter) >= 1:
        luvcol += name2.count(letter)

strScore = str(trucol) + str(luvcol)
final = int(strScore)
if final < 10 or final > 90:
    print(f"Your score is {final}, you go together like coke and mentos.")
elif final >= 40 and final <= 50:
    print(f"Your score is {final}, you are alright together.")
else:
    print(f"Your score is {final}.")
