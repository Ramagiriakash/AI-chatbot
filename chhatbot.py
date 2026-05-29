import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

print("AI Chatbot Started")
print("Type 'exit' to stop")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Chatbot Stopped")
        break

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    answer = response.choices[0].message.content

    print("Bot:", answer)
 
