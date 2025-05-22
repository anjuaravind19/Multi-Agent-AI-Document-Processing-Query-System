from fastapi import FastAPI
from pydantic import BaseModel
from shared.agent import get_agent
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from fastapi import HTTPException

load_dotenv()

app = FastAPI()
agent = get_agent()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_agent(query: Query):
    try:
        response = agent.run(query.question)
        return {"answer": response}
    except Exception as e:
        print(f"Error in agent: {e}")
        raise HTTPException(status_code=500, detail="Agent failed to respond.")
"""def ask_agent(query: Query):
    response = agent.run(query.question)
    return {"answer": response}"""
