# turn each word in to a key with it's length as the value using dictionary comprehension
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word: len(word) for word in sentence.split()}

print(result)

