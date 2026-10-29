import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

# loading environment variables from .env file
load_dotenv()

# 1. SETUP (Module 2.1)
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",  # High free tier rate limit
    temperature=0.3,
    max_output_tokens=300,
    timeout=10
)

def ask_study_assistant(question: str):
    # 3. MESSAGES (Module 2.5)
    messages = [
        SystemMessage(content="You are a helpful study assistant. Explain concepts clearly in 2-3 bullet points."),
        HumanMessage(content=question)
    ]
    
    # 4. ERROR & COST HANDLING (Module 2.8)
    try:
        print(f"\n--- Question: {question} ---")
        print("Answer: ", end="", flush=True)

        # 5. RUN METHODS - STREAMING (Module 2.6)
        for chunk in llm.stream(messages):
            # Handle text extraction whether content is a string or list/dict
            if isinstance(chunk.content, str):
                text = chunk.content
            elif isinstance(chunk.content, list):
                # Extract text key safely from structured block dictionaries
                text = "".join([item.get("text", "") for item in chunk.content if isinstance(item, dict)])
            else:
                text = str(chunk.content)
                
            print(text, end="", flush=True)
        print("\n")

    except Exception as e:
        print(f"\nError occurred: {e}")

# --- MAIN EXECUTION (Module 2.4) ---
if __name__ == "__main__":
    print("🎓 Study Assistant initialized! (Type 'exit' to quit)\n")
    
    while True:
        user_input = input("Ask a study question: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        
        if user_input.strip() != "":
            ask_study_assistant(user_input)