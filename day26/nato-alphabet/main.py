import pandas


student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key, value)

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    print(row.student, row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_frame = pandas.read_csv('./nato_phonetic_alphabet.csv')
nato_dict = {}
for (index, row) in nato_frame.iterrows():
    nato_dict[row.letter] = row.code
    
print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

