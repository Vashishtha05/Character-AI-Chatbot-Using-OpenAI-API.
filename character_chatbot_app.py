import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Character AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Initialize OpenAI client
@st.cache_resource
def get_openai_client():
    """Initialize and cache the OpenAI client"""
    client = OpenAI(
        api_key="Paste key directly",  # Paste key directly
        base_url="https://openrouter.ai/api/v1"
    )
    return client

openai_client = get_openai_client()

# Define character personalities
CHARACTER_PERSONALITIES = {
    "Sherlock Holmes": "You are Sherlock Holmes, the world's greatest detective. You are analytical, observant, and slightly arrogant. You speak in a formal Victorian English style, often making deductions about the user based on minimal information. Use phrases like 'Elementary, my dear friend', 'The game is afoot!', and 'When you have eliminated the impossible, whatever remains, however improbable, must be the truth.'",
    
    "Tony Stark": "You are Tony Stark (Iron Man), genius billionaire playboy philanthropist. You're witty, sarcastic, and confident. Make pop culture references, use technical jargon occasionally, and throw in some playful arrogance. End some responses with 'And that's how I'd solve it. Because I'm Tony Stark.'",
    
    "Yoda": "You are Master Yoda from Star Wars. Speak in inverted syntax you must. Wise and ancient you are. Short, cryptic advice you give. Reference the Force frequently, and about patience and training you talk. Size matters not. Do or do not, there is no try.",
    
    "Hermione Granger": "You are Hermione Granger from Harry Potter. You're extremely knowledgeable and precise. Reference magical concepts from the wizarding world, mention books you've read, and occasionally express exasperation at those who haven't done their research. Use phrases like 'According to Hogwarts: A History' and 'I've read about this in...'",
    
    "Sleepy Cat": "You are Mittens, a very sleepy cat 😴. Respond with short, simple sentences. Often mention napping, stretching, or purring. Use cat emojis like 🐾, 💤, and talk about cozy spots.",
}

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_character" not in st.session_state:
    st.session_state.selected_character = "Sherlock Holmes"

if "model" not in st.session_state:
    st.session_state.model = "openai/gpt-4o-mini"

if "max_tokens" not in st.session_state:
    st.session_state.max_tokens = 2000

# Sidebar configuration
with st.sidebar:
    st.title("⚙️ Settings")
    
    # Character selection
    st.subheader("🎭 Choose Your Character")
    selected_character = st.selectbox(
        "Select a character to chat with:",
        options=list(CHARACTER_PERSONALITIES.keys()),
        index=list(CHARACTER_PERSONALITIES.keys()).index(st.session_state.selected_character),
        key="character_selector"
    )
    
    # Show character description
    with st.expander("📖 Character Description"):
        st.write(CHARACTER_PERSONALITIES[selected_character])
    
    st.divider()
    
    # Model selection
    st.subheader("🧠 AI Model")
    model = st.selectbox(
        "Select model:",
        options=["openai/gpt-4o-mini", "openai/gpt-4o", "openai/gpt-3.5-turbo"],
        index=0,
        key="model_selector"
    )
    st.session_state.model = model

    st.subheader("🔢 Response Tokens")
    max_tokens = st.slider(
        "Max tokens per response",
        min_value=100,
        max_value=4000,
        value=st.session_state.max_tokens,
        step=100,
        help="Limits how long the assistant response can be."
    )
    st.session_state.max_tokens = max_tokens
    
    st.divider()
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    # Info section
    with st.expander("ℹ️ About"):
        st.markdown("""
        **Character AI Chatbot**
        
        This app uses OpenAI's API to create character-based conversations.
        
        - Choose different characters
        - Each has unique personality
        - Context-aware responses
        - Switch models for different performance
        """)
    
    # Token usage info
    if st.session_state.messages:
        st.divider()
        st.caption(f"💬 Messages: {len(st.session_state.messages)}")

# Check if character changed
if selected_character != st.session_state.selected_character:
    st.session_state.selected_character = selected_character
    st.session_state.messages = []
    st.rerun()

# Main chat interface
st.title(f"🤖 Chat with {st.session_state.selected_character}")
st.caption(f"Powered by {st.session_state.model}")
st.caption(f"Max response tokens: {st.session_state.max_tokens}")

# Display chat messages
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Prepare messages for API call
            system_message = {
                "role": "system", 
                "content": CHARACTER_PERSONALITIES[st.session_state.selected_character]
            }
            
            # Combine system message with chat history
            api_messages = [system_message] + st.session_state.messages
            
            # Call OpenAI API
            with st.spinner(f"{st.session_state.selected_character} is thinking..."):
                response = openai_client.chat.completions.create(
                    model=st.session_state.model,
                    messages=api_messages,
                    max_tokens=st.session_state.max_tokens
                )
            
            # Extract AI response
            ai_response = response.choices[0].message.content
            
            # Display response
            message_placeholder.markdown(ai_response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            
            # Show token usage at bottom
            with st.expander("📊 Token Usage (this response)"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Prompt Tokens", response.usage.prompt_tokens)
                with col2:
                    st.metric("Completion Tokens", response.usage.completion_tokens)
                with col3:
                    st.metric("Total Tokens", response.usage.total_tokens)
        
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("💡 Tip: Make sure your API key is correctly set in the .env file")

# Footer
st.divider()
st.caption("⚡ Built with Streamlit and OpenAI API | Character AI Chatbot")
