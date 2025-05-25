import os
import requests
import json
import anthropic

client= anthropic.Client(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages =[
        {"role":"user", "content":"How can I get started with claude4?"}
    ]
)

print(message.content)