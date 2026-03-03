# 🎭 Character AI Chatbot — Streamlit LLM App

<p align="center">
  <img src="https://img.shields.io/badge/LLM-OpenAI%20API-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Streamlit-Interactive%20App-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-Chatbot-yellow?style=for-the-badge">
  <img src="https://img.shields.io/badge/GenAI-Character%20Simulation-green?style=for-the-badge">
</p>

<p align="center">
  An interactive Character AI chatbot built with Streamlit and OpenAI-compatible APIs.
</p>

---

## 📌 Overview

This project implements a **multi-character conversational AI application** where users can interact with predefined personalities powered by LLMs.

The app supports:

- Real-time chat interface  
- Multiple character personas  
- Model switching  
- Token usage tracking  
- Clean, responsive Streamlit UI  

---

## ✨ Features

- 🎭 Multiple character personalities  
- 💬 Real-time conversation with memory  
- 🧠 Model selection (GPT-4o, GPT-4o-mini, GPT-3.5-turbo)  
- 📊 Token usage monitoring  
- 🔄 Clear chat history option  
- 🎨 Simple and responsive interface  

---

## 🧠 Available Characters

- **Sherlock Holmes** — Analytical detective with formal tone  
- **Tony Stark** — Witty and sarcastic innovator  
- **Yoda** — Wise mentor using inverted syntax  
- **Hermione Granger** — Knowledgeable and detail-oriented  
- **Sleepy Cat** — Relaxed and drowsy personality  

---

## ⚙️ Tech Stack

| Technology | Usage |
|------------|--------|
| Python | Core development |
| Streamlit | Web interface |
| OpenAI / OpenRouter API | LLM inference |
| python-dotenv | Environment management |

---

## 🚀 Getting Started

### 1️⃣ Install Dependencies

```bash
pip install streamlit openai python-dotenv
```

### 2️⃣ Configure API Key

Create a `.env` file:

```env
OPENROUTER_API_KEY=your-api-key-here
```

### 3️⃣ Run the Application

```bash
streamlit run character_chatbot_app.py
```

The app runs at:

```
http://localhost:8501
```

---

## 🖥️ How It Works

1. User selects a character from the sidebar  
2. User selects an LLM model  
3. Messages are sent to the API  
4. Responses are generated using character-specific system prompts  
5. Token usage is displayed per interaction  

---

## 📄 Notes

- Switching characters resets conversation history  
- Token tracking helps monitor API usage  
- Compatible with OpenRouter’s OpenAI-style endpoint  

---

## 👨‍💻 Author 
**Vashishtha Verma** 
* 🤖 Machine Learning & Generative AI
* 🧠 Agentic AI Systems
* 💻 Software Engineering & DSA
