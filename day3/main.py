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
prompt1="HI"
prompt2="Explain Time travell in detail"
prompt3="write love letter in 1000 words to a girl name Nastaran"

Prompts=[prompt1,prompt2,prompt3]

for prompt_pointer in Prompts:
    message={
    "role":role,
    "content":prompt_pointer
}
    messages=[message]

    response=client.chat.completions.create(model=model,messages=messages,max_tokens=100)

    print(f"Prompt: {prompt_pointer} -->your tokens: {response.usage.prompt_tokens} completion_tokens: {response.usage.completion_tokens} total tokens: {response.usage.total_tokens}")
    print(f"Finish reason: {response.choices[0].finish_reason}")






