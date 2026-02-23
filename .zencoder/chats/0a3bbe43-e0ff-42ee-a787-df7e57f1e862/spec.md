# Technical Specification: Conversation History for ChatAgent

## 1. Technical Context
- **Language**: Python 3.13
- **Frameworks**: FastAPI, LangChain (langchain_ollama), MCP
- **LLM**: Ollama (qwen2.5:7b-instruct)
- **Complexity**: easy

## 2. Implementation Approach
- **Conversation State**: Add a list to `ChatAgent` to store message history (HumanMessage, AIMessage, ToolMessage).
- **Message Handling**: Update `ChatAgent.run` to append the user's query and the LLM's response to the history.
- **LLM Integration**: Update `llm_ollama.call_llm` to accept a list of LangChain messages instead of just a prompt string.
- **Prompting**: Update `prompt.py` to generate a system message instead of a flat prompt string, or incorporate the history into the template.

## 3. Source Code Changes
- `AI-Assistant/agent.py`: 
    - Initialize `self.history` in `ChatAgent.__init__`.
    - Update `run()` to manage the history list.
- `AI-Assistant/llm_ollama.py`: 
    - Update `call_llm(input: Union[str, List[BaseMessage]], ...)` to handle both types.
- `AI-Assistant/prompt.py`: 
    - Refactor `get_prompt` to return a system message or adjust it for a message-based workflow.

## 4. Data Model / API Changes
- No immediate API changes required to `main.py` for a single-session proof of concept.
- Future enhancement: Support `session_id` in the `/chat` endpoint.

## 5. Verification Approach
- **Manual Test**: Send a query (e.g., "My name is Shreyash"), followed by a second query ("What is my name?").
- **Linting**: Run `flake8` or similar if available.
- **Logging**: Ensure tool calls and history updates are visible in logs.
