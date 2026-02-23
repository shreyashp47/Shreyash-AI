from fastapi import FastAPI, HTTPException, Form
from agent import ChatAgent

app = FastAPI()

chat_agent = ChatAgent()

@app.post("/chat")
async def chat(
    query: str = Form(...)
):
    """
    Handles chat requests from clients.
    Validates the query input and processes it through the ChatAgent.
    Returns the AI-generated answer.
    """
    if not query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    result = await chat_agent.run(query)

    return {
        "answer": result
    }