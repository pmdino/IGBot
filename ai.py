import openai
import os
from dotenv import load_dotenv

load_dotenv('./.env')
openai.api_key = os.environ['OPENAI_API_KEY']

def ask(question, prompt):
    prompt += (str(question) + '\n')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    answer = str(response.choices[0].text)
    prompt += (answer + '\n')
    return answer, prompt
