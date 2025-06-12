import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class SkillAgent:
    def __init__(self, client, system_prompt):
        self.client = client
        self.system = system_prompt
        self.messages = [{"role": "system", "content": self.system}]

    def __call__(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        return self.execute()

    def execute(self):
        response = self.client.chat.completions.create(
            model="llama3-70b-8192",
            messages=self.messages
        )
        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        return reply