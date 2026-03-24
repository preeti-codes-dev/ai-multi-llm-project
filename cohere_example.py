import cohere
from utils.config import COHERE_API_KEY

co = cohere.ClientV2(COHERE_API_KEY)

def generate_text(prompt):
    response = co.chat(
        model="command-a-03-2025",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.message.content[0].text

if __name__ == "__main__":
    try:
        prompt = input("Enter prompt: ")
        print(generate_text(prompt))
    except Exception as e:
        print("Error:", e)