from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_community.tools.arxiv.tool import ArxivQueryRun
from langchain.tools.retriever import create_retriever_tool
from langchain_groq import ChatGroq
from shared.vector import get_retriever
import os

def get_agent():
    retriever = get_retriever()
    retriever_tool = create_retriever_tool(
        retriever,
        name="file_qa_tool",
        description="Answer questions based on uploaded documents"
    )

    arxiv_tool = ArxivQueryRun()

    tools = [retriever_tool, arxiv_tool]

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile" #gemma-7b-it"
    )

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True
    )

    return agent
