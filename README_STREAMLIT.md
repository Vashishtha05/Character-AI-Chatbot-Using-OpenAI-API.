# Character AI Chatbot - Streamlit App

This is a Streamlit web application converted from the Jupyter notebook that creates an interactive Character AI Chatbot using OpenAI's API.

## Features

- 🎭 **Multiple Characters**: Choose from Sherlock Holmes, Tony Stark, Yoda, Hermione Granger, or Sleepy Cat
- 💬 **Real-time Chat**: Interactive chat interface with conversation history
- 🧠 **Model Selection**: Switch between different OpenAI models (GPT-4o, GPT-4o-mini, GPT-3.5-turbo)
- 📊 **Token Tracking**: View token usage for each response
- 🎨 **Clean UI**: Modern, responsive interface built with Streamlit

## Prerequisites

Make sure you have the following installed:
- Python 3.8+
- pip

## Installation

1. **Install required packages**:
```bash
pip install streamlit openai python-dotenv
```

2. **Set up your environment variables**:
Create a `.env` file in the same directory with your OpenRouter API key:
```
OPENROUTER_API_KEY=your-api-key-here
```

## Running the App

Navigate to the directory containing the app and run:

```bash
streamlit run character_chatbot_app.py
```

The app will open automatically in your default web browser at `http://localhost:8501`

## How to Use

1. **Select a Character**: Use the sidebar to choose which character you want to chat with
2. **Choose a Model**: Select the AI model (GPT-4o-mini is recommended for cost-effectiveness)
3. **Start Chatting**: Type your message in the input box at the bottom
4. **View Token Usage**: Expand the token usage section after each response to see consumption
5. **Clear History**: Click the "Clear Chat History" button to start fresh

## Character Personalities

- **Sherlock Holmes**: Analytical detective with formal Victorian English
- **Tony Stark**: Witty, sarcastic genius billionaire
- **Yoda**: Wise Jedi Master speaking in inverted syntax
- **Hermione Granger**: Knowledgeable wizard with references to magical world
- **Sleepy Cat**: A very drowsy feline friend 😴

## Troubleshooting

- **API Key Error**: Make sure your `.env` file is in the correct directory and contains a valid OPENROUTER_API_KEY
- **Module Not Found**: Install missing packages using `pip install package-name`
- **Port Already in Use**: If port 8501 is busy, Streamlit will automatically try the next available port

## Notes

- Each character switch clears the chat history to maintain personality consistency
- Token usage is tracked per response to help monitor API costs
- The app uses OpenRouter's API endpoint compatible with OpenAI SDK

## Credits

Based on the "Build a Character AI Chatbot Using OpenAI API" Jupyter notebook.
