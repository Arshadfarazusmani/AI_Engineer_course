## BOILER PLATE 
```python
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
```






ChatCompletion(id='chatcmpl-ae2664af-9d47-4326-a8dd-b2f693cc6502', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='Hello! How can I help you today?', role='assistant', annotations=None, executed_tools=None, function_call=None, reasoning='We just need to greet. Probably respond "Hello! How can I help you today?"', tool_calls=None))], created=1790339224, model='openai/gpt-oss-20b', object='chat.completion', mcp_list_tools=None, service_tier='on_demand', system_fingerprint='fp_1074f9ce08', usage=CompletionUsage(completion_tokens=37, prompt_tokens=72, total_tokens=109, completion_time=0.038609617, completion_tokens_details=CompletionTokensDetails(reasoning_tokens=19), prompt_time=0.003458165, prompt_tokens_details=None, queue_time=0.337305144, total_time=0.042067782), usage_breakdown=None, x_groq=XGroq(id='req_01m3c8h43tepfs4a032pb0jak0', debug=None, seed=1773631350, usage=None))