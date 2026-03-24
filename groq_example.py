from groq import Groq
from utils.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def generate_text(prompt):
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant"
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    try:
        prompt = input("Enter prompt: ")
        print(generate_text(prompt))
    except Exception as e:
        print("Error:", e)