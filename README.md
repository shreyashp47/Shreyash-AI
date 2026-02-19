

# AI Assistant Local-MCP-Ollama-Setup

This guide explains how to set up a local AI Assistant using:

* Ollama
* Visual Studio Code
* Postman
* Python backend (MCP Server)

Everything runs on a local machine.

---

## 1. Install Ollama

Download and install: [https://ollama.com](https://ollama.com)

```bash
ollama --version  # Verify installation
```

---

## 2. Download a Model

Example model: [https://ollama.com/library/qwen2.5:7b-instruct](https://ollama.com/library/qwen2.5:7b-instruct)

```bash
ollama pull qwen2.5:7b-instruct  # Pull the model
```

```bash
ollama run qwen2.5:7b-instruct  # Run the model
```

If it responds in terminal, setup is correct.

---

## 3. Model Location (Mac)

```
/Users/shreyash/.ollama/models   # Default model path on my mac | check model location in Ollama settings.
```

---

## 4. Test Ollama via API

Test using Postman: [Ollama DOC](https://docs.ollama.com/api/chat)

POST

```
http://localhost:11434/api/chat
```

Body → JSON:

```json
{
  "model": "qwen2.5:7b-instruct",
  "messages": [
      {"role": "system","content": "You are helpfull AI assistant"},
      {"role": "user","content": "Explain the reflection"}
  ],
  "stream": false
}
```

---

## 5. Create Two Projects

Create two empty projects:

* mcp-server
* Ai-Assistant

Open both in separate Visual Studio Code windows.

---

## 6. Create Virtual Environment (Python 3.13)

Inside each project:

```bash
python3.13 -m venv .venv
```

Activate virtual environment (Mac/Linux):

```bash
source .venv/bin/activate
```

---
Add the following section after the virtual environment step in your `README.md`.

---

## 7. Install Required Dependencies

Create a `requirements.txt` file inside both projects 

Add the required dependencies in `requirements.txt`

```bash
pip install -r requirements.txt   # Install dependencies:
```

Verify installation:

```bash
pip list  #Now your environment is ready to build the MCP server and backend API.
```
---

## 8. Create `main.py` in  AI Assistant project and Run Server

Create a `main.py` file inside your project.

Run the server:

```bash
UVICORN_HOST=127.0.0.1 UVICORN_PORT=9001 uvicorn main:app --reload
```
--- 
## 9. Setup MCP Server

Create a new empty project for the MCP server and open it in Visual Studio Code.

Create a virtual environment (if not already created):

```bash
python3.13 -m venv .venv
source .venv/bin/activate
```

Create a `requirements.txt` file and add the dependencies mentioned in Step 7.

Install dependencies:

```bash
pip install -r requirements.txt
```

Copy the `main.py` file into this MCP project.  
(Implementation details will be added in the repository.)

---

### Install `uv`

Install `uv` using terminal:

```bash
pip install uv
```

Verify installation:

```bash
uv --version
```

---

### Run MCP Server

```bash
uv run main.py
```
---
Add the following correction under your AI Assistant server section.

---

### Test AI Assistant API (Postman)

```
http://127.0.0.1:9001/chat
```
Body → JSON:

```json
{
  "query": "What is the current bitcoin price"
}
```
 
---

This repository is for learning and personal experimentation with local AI systems and MCP architecture.
