import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

My_api_key=os.getenv("GROQ_API_KEY")

if not My_api_key:
    raise ValueError("API NOT FOUND")

client= Groq(api_key=My_api_key)
model="openai/gpt-oss-20b"
role ="user"
prompt="hi"

message={
    "role":role,
    "content":prompt
}

messages=[message]

response=client.chat.completions.create(model=model,messages=messages)

print(response)