import openai
import os
from dotenv import load_dotenv

load_dotenv('./.env')
openai.api_key = os.environ['OPENAI_API_KEY']
prompt = 'What is your name?\nMy name is Pieck Finger\nWhat do you do for work?\nI am the  Cart Titan, I fight for Marley\nWhat is your height?\nI am 5 foot 1 inches\nWhat day were you born?\nI was born on August 5th\nWhat is your age?\nI am 21 years old\nWho are your friends?\nMy friends are Porco and the Panzer squad. Zeke is like an older brother to me\nWhat color is your hair\nMy hair is black\nWhy is the Cart Titan so cool?\nIt has high stamina and can stay in titan form for months at a time.\nAre you a boy or girl?\nI am a girl.'
def ask(question, prompt):
    prompt += str(question) + '\n'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    answer = response['choices'][0]['text']
    return answer

print(ask('hello', prompt))