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
prompt="Suggest name for my Softwware Agency"

message_system={
    "role":"system",
    "content":"You Are brand manager who suggest the brand name for my company,give in one word "
}
message={
    "role":role,
    "content":prompt
}



messages=[message_system,message]

response=client.chat.completions.create(model=model,messages=messages,temperature=2)

print(response.choices)