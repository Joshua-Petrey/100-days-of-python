import requests as r
# get ten random questions from the openTriviaDB
data = r.get("https://opentdb.com/api.php?amount=10&type=boolean").json()

question_data = []
# convert the returned json into a dictionary
for x in data['results']:
    question_data.append({'text': x['question'], 'answer': x['correct_answer']})
