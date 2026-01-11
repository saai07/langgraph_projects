from typing import TypedDict , List
from langgraph.graph import START , END , StateGraph
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    message: List[HumanMessage]
    
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


def process(state:AgentState) -> AgentState:
    response = llm.invoke(state["message"])
    print("Agent Response:", response.content)
    return state

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)

agent = graph.compile()

user_input = input("Enter your message , to exit type 'exit' ")
while user_input.lower() != "exit":
    agent.invoke({"message":[HumanMessage(content=user_input)]})
    user_input = input("Enter your message :")