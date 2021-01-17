import pandas

# Create a dictionary from nato_frame
nato_frame = pandas.read_csv('./nato_phonetic_alphabet.csv')
nato_dict = {}
for (index, row) in nato_frame.iterrows():
    nato_dict[row.letter] = row.code

print(nato_dict)

# code_words stores translated codes
code_words = []
# get text users wants translated
user_word = input('Enter a word').upper()

# for each letter in user_word return the mapped value from nato_dict
code_words = [nato_dict[letter] for letter in user_word]

print(code_words)
