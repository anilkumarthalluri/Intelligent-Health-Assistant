import os
import streamlit as st
from groq import Groq

class AI:
    def __init__(self):
        """Initializes the Groq client, trying Streamlit secrets first."""
        try:
            # Recommended for deployment: Use Streamlit's secrets management
            api_key = st.secrets["GROQ_API_KEY"]
        except (FileNotFoundError, KeyError):
            # Fallback for local development: Use environment variables
            from dotenv import load_dotenv
            load_dotenv()
            api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found. Please set it in your Streamlit secrets or a local .env file.")

        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"  # Change model name if needed

    def get_response(self, messages):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()

    def get_response_stream(self, messages):
        """Yields response chunks as they are generated."""
        return self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
            max_tokens=1000,
            stream=True  # Enable streaming
        )

    def process_stream(self, messages):
        """Gets and processes the stream, yielding only the content strings."""
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
            max_tokens=1000,
            stream=True
        )
        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content is not None:
                yield content