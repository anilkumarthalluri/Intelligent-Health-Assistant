# 🩺 Intelligent Health Assistant

This project is an AI-powered health assistant chatbot built with Streamlit. It provides a conversational interface for users to ask general health-related questions and receive informative responses from a powerful large language model (LLM).

## ✨ Features

- **Conversational AI**: Engage in a natural, chat-like conversation.
- **Streaming Responses**: The assistant's replies are streamed in real-time for a more interactive experience.
- **"New Chat" Functionality**: Easily clear the conversation history and start fresh.
- **Informative Sidebar**: Includes details about the application and links to reputable health resources like WebMD, Mayo Clinic, and WHO.
- **Clean, User-Friendly Interface**: Built with Streamlit for a simple and intuitive user experience.

## 🛠️ Technology Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - For creating the web application interface.
- **Backend/AI**:
    - [Groq](https://groq.com/) - Provides fast inference for the language model.
    - **Llama 3.3 70B**: The large language model used for generating responses.
- **Language**: Python

## ⚙️ Setup and Installation

Follow these steps to set up and run the project locally.

### 1. Prerequisites

- Python 3.8 or higher
- A Groq API key. You can get one from the [Groq Console](https://console.groq.com/keys).

### 2. Clone the Repository

```bash
git clone <your-repository-url>
cd ai-chatbot-main
```

### 3. Install Dependencies

Install the required Python libraries using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a file named `.env` in the root directory of the project and add your Groq API key to it.

```
# .env
GROQ_API_KEY="your_groq_api_key_here"
```

**Note**: The `aimedic.py` file uses `python-dotenv` to load this key.

## 🚀 Running the Application

Once the setup is complete, you can run the Streamlit application with the following command:

```bash
streamlit run main.py
```

This will start a local web server, and you can access the Intelligent Health Assistant in your browser at `http://localhost:8501`.