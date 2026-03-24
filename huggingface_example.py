from huggingface_hub import InferenceClient
from utils.config import HUGGINGFACE_API_KEY

client = InferenceClient(api_key=HUGGINGFACE_API_KEY)

def generate_text(prompt):
    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    try:
        prompt = input("Enter prompt: ")
        print(generate_text(prompt))
    except Exception as e:
        print("Error:", e)