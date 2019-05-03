import numpy as np
import pandas as pd


"""
with open('../data/questions.txt') as f:
    content = f.readlines()
questions = [x.strip() for x in content]

with open('../data/answers.txt') as f:
    content = f.readlines()
answers = [x.strip() for x in content]

df = pd.DataFrame(
    {'Questions': questions,
     'Answers': answers
    })

df.to_csv('../data/faq.csv', encoding='utf-8', index=False)
"""

df = pd.read_csv('../data/faq.csv')
questions = df.iloc[:, 0].values
answers = df.iloc[:, 1].values

dict = {}
for i in range(len(questions)):
    dict[questions[i]] = answers[i]

