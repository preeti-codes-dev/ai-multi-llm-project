import ollama

def generate_text(prompt):
    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]

if __name__ == "__main__":
    try:
        prompt = input("Enter prompt: ")
        print(generate_text(prompt))
    except Exception as e:
        print("Error:", e)