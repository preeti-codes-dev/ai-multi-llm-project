from google import genai
from utils.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_text(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    try:
        prompt = input("Enter prompt: ")
        print(generate_text(prompt))
    except Exception as e:
        print("Error:", e)