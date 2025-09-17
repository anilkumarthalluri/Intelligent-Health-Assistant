import streamlit as st
from aimedic import AI

st.set_page_config(page_title="Intelligent Health Assistant", page_icon="🩺", layout="centered", initial_sidebar_state="expanded")

def reset_chat():
    """Resets the chat history to its initial state."""
    st.session_state.messages = [{"role": "system", "content": "You are a helpful healthcare assistant."}]
    st.rerun()

with st.sidebar:
    st.subheader("Controls")
    if st.button("➕ New Chat", use_container_width=True):
        reset_chat()
    st.divider()
    st.subheader("About")
    st.markdown("""
    This Intelligent Health Assistant is a conversational AI designed to provide general health-related information.
    """)
    st.divider()
    st.subheader("Resources")
    st.markdown("""
    - [WebMD](https://www.webmd.com/)
    - [Mayo Clinic](https://www.mayoclinic.org/)
    - [World Health Organization (WHO)](https://www.who.int/)
    """)

st.markdown("<h1>🩺 Intelligent Health Assistant</h1>", unsafe_allow_html=True)
st.markdown("Your personal AI-powered guide for health-related questions. Start a conversation below.")

# Initialize chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful healthcare assistant."}]

# Display chat messages from history on app rerun
for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

# Chat input
if user_input := st.chat_input("What's on your mind ?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    # Display user message in chat message container
    st.chat_message("user").write(user_input)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        try:
            ai = AI()
            processed_stream = ai.process_stream(st.session_state.messages) # Get the processed text stream
            # Display the stream and capture the full response
            full_response = st.write_stream(processed_stream)
            # Add the assistant's response to the chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            st.error(f"❌ Error: {e}")