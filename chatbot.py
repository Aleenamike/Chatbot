from openai import OpenAI
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Initialize client with hidden API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chatbot(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",   # or gpt-4o-mini if available
        messages=[
            {"role": "system", "content": "You are a helpful chatbot."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Chat loop
print("🤖 Chatbot is ready! (type 'exit' to quit)\n")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye 👋")
        break
    bot_reply = chatbot(user_input)
    print("Bot:", bot_reply, "\n")
