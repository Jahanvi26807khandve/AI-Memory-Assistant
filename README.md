# AI Memory Assistant

A beginner-friendly AI project built with Python, Mem0, and Google Gemini.

## Overview

The AI Memory Assistant saves information provided by a user, retrieves relevant memories when questions are asked, and uses Gemini to generate answers based on the retrieved context.

## Features

- Save personal notes and preferences as memories
- Search for relevant memories using Mem0
- Generate contextual answers using Google Gemini
- View saved memories
- Interactive command-line menu

## Tech Stack

- **Python** — application logic
- **Mem0** — memory storage and retrieval
- **Google Gemini API** — AI-generated answers
- **python-dotenv** — secure environment variable loading

## How It Works

1. The user saves a memory.
2. Mem0 stores the information.
3. The user asks a question.
4. Mem0 retrieves relevant memories.
5. Gemini uses the retrieved context to generate an answer.

## Setup

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.
4. Create a `.env` file containing your Mem0 and Gemini API keys.
5. Run the application using `python main.py`.

## Environment Variables

- `MEM0_API_KEY`
- `GEMINI_API_KEY`

Never upload API keys or your `.env` file to GitHub.

## Learning Outcomes

- Working with third-party APIs
- Environment variables and secret management
- Python functions and control flow
- Memory retrieval and prompt construction
- Integrating a language model into an application

## Future Improvements

- Delete individual memories
- Add a graphical user interface
- Improve error handling
- Add automated tests
- Support multiple user profiles
