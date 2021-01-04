import requests

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

# get a random word from api
req = requests.get(
    'https://random-word-api.herokuapp.com/word?number=1').json()
# the word the api returned
word = req[0]

# create the blanks 
blank = []
for x in word:
    blank += "_"

print(logo)

end_of_game = False
num_of_tries = 6

while not end_of_game:
    guess = input("Guess a letter.").lower()

    if guess in blank:
        print(f"You already guessed {guess}")

    for letter in range(0, len(word)):
        if guess == word[letter]:
            blank[letter] = guess
            print(blank)

    if guess not in word:
        num_of_tries -= 1
        print(
            f"The letter {guess} is not in the word\n You have {num_of_tries} remaining")
        print(stages[num_of_tries])
        print(blank)

    if blank.count("_") == 0:
        print(f"You win the word was {word}")
        end = True

    if num_of_tries == 0:
        print(f"You have no tries remaing GAME OVER\nThe word was {word}")
        end = True
