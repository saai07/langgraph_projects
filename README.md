# Lang Graph Projects

A small collection of Python scripts and Jupyter notebooks exploring agent patterns and control flow using LangGraph/LangChain with Google Gemini (via `langchain-google-genai`). It includes a simple chat agent, memory logging, and several graph execution examples (sequential, conditional, looping, and multi-agent).

## Features

- Chat agent script powered by Gemini.
- Memory-enabled agent that logs conversations to a text file.
- LangGraph notebooks showcasing:
  - Simple flow
  - Sequential steps
  - Conditional routing
  - Looping graphs
  - Multiple/parallel agents

## Prerequisites

- Python 3.10+ (Windows, macOS, or Linux)
- A Google Generative AI API key

## Quick Start

1. Create and activate a virtual environment (Windows PowerShell):
   ```powershell
   python -m venv env
   .\env\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

3. Set your API key (Windows PowerShell):
   ```powershell
   $env:GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
   ```
   On macOS/Linux (bash/zsh):
   ```bash
   export GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
   ```

## Project Structure

- `Agent_bot.py`: Simple chat agent script using Gemini via LangChain.
- `memory_Agent.py`: Chat agent that persists conversation logs to `conversation_log.txt`.
- `check.py`: Minimal sanity-check/example runner.
- `conversation_log.txt`: Output log file for the memory agent.
- Notebooks:
  - `simple.ipynb`: Minimal LangGraph example.
  - `sequential.ipynb`: Sequential graph execution.
  - `conditional_Agent.ipynb`: Conditional routing within a graph.
  - `loop_graph.ipynb`: Looping/retry patterns.
  - `multiple.ipynb`: Multi-agent or parallel flows.

## Running

- Chat agent:
  ```powershell
  python Agent_bot.py
  ```

- Memory agent (writes to `conversation_log.txt`):
  ```powershell
  python memory_Agent.py
  ```

- Quick check:
  ```powershell
  python check.py
  ```

- Notebooks:
  ```powershell
  pip install jupyter ipykernel
  jupyter notebook
  ```
  Open the desired `.ipynb` and run cells.

## Notes & Troubleshooting

- If you see `NameError: ChatGoogleGenerativeAI is not defined`, install and import the provider:
  ```powershell
  pip install langchain-google-genai
  ```
  ```python
  from langchain_google_genai import ChatGoogleGenerativeAI
  llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
  ```
- Ensure `GOOGLE_API_KEY` is set in your environment before running scripts.
- Some notebooks may require additional packages; install as prompted.

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Google Generative AI](https://ai.google.dev/)
