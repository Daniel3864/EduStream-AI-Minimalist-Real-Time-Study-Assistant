# 🎓 EduStream AI: Minimalist Real-Time Study Assistant

A lightweight, single-file AI-powered Q&A tool built with Python, LangChain, and Google's Gemini API (`gemini-3.5-flash-lite`). It delivers low-latency, bullet-point study summaries directly in your terminal using real-time token streaming.

---

## 🚀 Features

* **Real-Time Token Streaming:** Outputs answers live as they are generated, eliminating waiting delays.
* **Structured Summaries:** Constrained via system instructions to provide concise 2–3 bullet point explanations.
* **Cost & Token Control:** Utilizes strict token caps (`max_output_tokens=300`) and temperature settings (`0.3`) for deterministic, cost-effective responses.
* **Secure Environment:** Loads API credentials safely from a local `.env` file.
* **Resilient Output Parsing:** Handles varying chunk data types (`str`, `list`, `dict`) seamlessly.

## ⚙️ Setup & Installation
### 1. Clone the Repository
Bash
git clone [https://github.com/Daniel3864/EduStream-AI-Minimalist-Real-Time-Study-Assistant.git](https://github.com/Daniel3864/EduStream-AI-Minimalist-Real-Time-Study-Assistant.git)
cd EduStream-AI-Minimalist-Real-Time-Study-Assistant
### 2. Install Dependencies
Bash
pip install python-dotenv langchain-google-genai langchain-core
### 3. Configure API Key
Create a .env file in the root directory and add your Google Gemini API key:
Code snippet
GOOGLE_API_KEY=your_actual_gemini_api_key_here

## 💻 Running the Application
Execute the Python script in your terminal or VS Code environment:
python app.py
Type any study topic or question (e.g., "What is Artificial Intelligence?") to receive a real-time streamed response. Type exit or quit to exit.

## 🔄 System Process Flow
Environment Initialization: Loads .env configuration securely.

Interactive Input: Listens for user questions in a terminal loop.

Payload Assembly: Packages system prompt constraints alongside user inputs.

API Dispatch: Sends requests to Google Gemini with hyperparameter enforcement (temperature, max_output_tokens).

Streaming & Normalization: Processes server-sent chunks and extracts raw text dynamically.

Console Output: Flushes formatted tokens directly to the terminal display.

---

## 🛠️ Project Structure

```text
StudyQA/
├── app.py              # Main application logic & CLI loop
├── .env                # Local environment secrets (API keys)
├── .gitignore          # Prevents tracking .env and bytecode
└── README.md           # Project documentation

