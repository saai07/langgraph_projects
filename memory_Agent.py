from typing import TypedDict , List , Union
from langgraph.graph import START , END , StateGraph
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage , AIMessage
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    MESSAGE: List[Union[HumanMessage , AIMessage]]
    
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def process(state:AgentState) -> AgentState:
    """Process the input messages and generate a response using the LLM."""
    response = llm.invoke(state["MESSAGE"])
    state["MESSAGE"].append(AIMessage(content=response.content))
    
    print(f"Agent Response: {response.content}")
    return state

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process" , END)

Agent = graph.compile()

conversation_history = []

user_input = input("Enter your message , to exit  type 'exit' ")

while user_input.lower() != "exit":
    conversation_history.append(HumanMessage(content=user_input))
    result = Agent.invoke({"MESSAGE": conversation_history})
    converstaion_history = result["MESSAGE"]
    user_input = input("Enter your message : ")
    
with open("conversation_log.txt", "w") as file:
    file.write("Conversation Log:\n")
    for message in conversation_history:
        if isinstance(message, HumanMessage):
            file.write(f"User: {message.content}\n")
        else:
            file.write(f"Agent: {message.content}\n\n")
    file.write( "End of conversation\n")
print("Conversation log saved to conversation_log.txt")