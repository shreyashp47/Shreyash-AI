# Shreyash-AI: a local AI agent with MCP tool calling

A small, fully local AI assistant. You ask a question over HTTP; a FastAPI agent shows a local
LLM (Ollama, `qwen2.5:7b-instruct`) the tools exposed by an MCP server, runs the tool the model
picks, then asks the model again so the final answer is grounded in the tool result.

No cloud LLM and no API keys: the model runs on your machine through Ollama, and the
assistant reaches its tools through the Model Context Protocol (MCP) over SSE.

## How it works

```
client ── POST /chat ──▶ AI-Assistant (FastAPI, :9001)
                           1. list the MCP server's tools          ──▶ mcp-ai-server (FastMCP, :8000/sse)
                           2. call qwen2.5 with the tool schemas          └─ get_crypto_price → CoinGecko API
                           3. if the model requests a tool, run it  ──▶
                           4. call the model again with the result
client ◀── {"answer": ...} ┘
```

| File | Role |
|---|---|
| `AI-Assistant/main.py` | FastAPI app with the `POST /chat` endpoint |
| `AI-Assistant/agent.py` | The tool-calling loop: list tools → LLM → run tool → LLM |
| `AI-Assistant/llm_ollama.py` | `ChatOllama` client (LangChain), temperature 0, tools bound per call |
| `AI-Assistant/mcp_client.py` | Lists and calls MCP tools over SSE |
| `AI-Assistant/prompt.py` | Prompt that makes the model answer from the tool result when there is one |
| `mcp-ai-server/main.py` | FastMCP server exposing `get_crypto_price` (CoinGecko) |

## Run it

**1. Ollama and the model**

Install [Ollama](https://ollama.com), then:

```bash
ollama pull qwen2.5:7b-instruct
ollama run qwen2.5:7b-instruct   # replies in the terminal = setup works
```

**2. MCP server** (terminal 1)

```bash
cd mcp-ai-server
python3.13 -m venv .venv && source .venv/bin/activate
pip install -r req.txt uv
uv run main.py                   # serves MCP over SSE at http://127.0.0.1:8000/sse
```

**3. AI assistant** (terminal 2)

```bash
cd AI-Assistant
python3.13 -m venv .venv && source .venv/bin/activate
pip install -r requirement.txt
UVICORN_HOST=127.0.0.1 UVICORN_PORT=9001 uvicorn main:app --reload
```

**4. Ask a question**

`/chat` reads a form field named `query`:

```bash
curl -X POST http://127.0.0.1:9001/chat -F "query=What is the current bitcoin price?"
```

The model sees `get_crypto_price`, calls it with `coin=bitcoin`, and answers with the live price.
For a question no tool covers, it answers from its own knowledge.

## Adding a tool

Add a function with `@mcp.tool(name=..., description=...)` in `mcp-ai-server/main.py` and restart
the server. The assistant lists tools on every request, so the model sees the new tool without any
change to `AI-Assistant`.

## Tips

- Test Ollama on its own with Postman or curl: `POST http://localhost:11434/api/chat`
  ([API docs](https://docs.ollama.com/api/chat)).
- Ollama stores models in `~/.ollama/models` by default; the Ollama settings show the location.

---

Built for learning and experimenting with local LLMs, agents and MCP.
