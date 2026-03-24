#  Multi-LLM API Integration Project

##  Overview

This project demonstrates how multiple Artificial Intelligence (AI) platforms can be connected and used in a single system.

In simple terms, the user enters a question (prompt), and the system generates a response using different AI models.


##  Objective

The main objectives of this project are:

- To understand how AI APIs work  
- To integrate multiple AI platforms in one project  
- To send user input and receive AI-generated responses  
- To handle errors properly when APIs fail  


##  What is Artificial Intelligence?

Artificial Intelligence (AI) is a technology that allows computers to think, learn, and respond like humans.

Examples:
- Chatbots  
- Voice assistants  
- Recommendation systems  

##  What I Did in This Project

In this project, I:

- Integrated multiple AI APIs  
- Created separate Python programs for each AI platform  
- Took user input from the keyboard  
- Sent the input to AI models  
- Displayed the response to the user  
- Handled errors such as API limits and quota issues  
- Organized the project with a clean folder structure  
- Uploaded the project to GitHub  


##  AI Platforms Used

This project includes the following AI services:

1. Groq – Fast AI response generation  
2. Cohere – Natural language processing  
3. Hugging Face – Open-source AI models  
4. Ollama – Local AI model (runs on system)  
5. Gemini – Google AI (may show quota error)  
6. OpenAI – Advanced AI models (may show quota error)  


##  How the Project Works

1. The user enters a prompt  
2. The program sends the prompt to an AI model  
3. The AI processes the request  
4. The response is displayed to the user  


##  How to Run the Project

### Step 1: Install dependencies
pip install -r requirements.txt


### Step 2: Run any file
python groq_example.py

You can also run:
python gemini_example.py
python cohere_example.py
python huggingface_example.py
python ollama_example.py
python openai_example.py

##  Screenshots

### Groq Output
![Groq Output](screenshots/groq_output.png)

### Cohere Output
![Cohere Output](screenshots/cohere_output.png)

### HuggingFace Output
![HuggingFace Output](screenshots/huggingface_output.png)

### Ollama Output
![Ollama Output](screenshots/ollama_output.png)

### Gemini Output (Quota Error)
![Gemini Output](screenshots/gemini_output.png)

### OpenAI Output (Quota Error)
![OpenAI Output](screenshots/openai_output.png)


##  Note

- Gemini and OpenAI APIs may show errors due to usage limits (quota exceeded)  
- These errors are handled properly in the code  
- Other APIs like Groq, Cohere, Hugging Face, and Ollama work successfully  


##  Project Structure
ai-multi-llm-project/
├── groq_example.py
├── cohere_example.py
├── huggingface_example.py
├── ollama_example.py
├── gemini_example.py
├── openai_example.py
├── utils/config.py
├── screenshots/
├── README.md


##  Security

- API keys are stored securely in a `.env` file  
- Sensitive information is not shared publicly  


##  Conclusion

This project successfully demonstrates how multiple AI models can be integrated into a single system.

It provides practical knowledge of:
- API integration  
- AI model usage  
- Error handling  
- Real-world AI applications  