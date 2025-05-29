import asyncio
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient
import os
from dotenv import load_dotenv

async def run_memory_chat():
    "Run a chat with built in MCP Agent's conversation memory"

    #Load env variable for API Keys
    load_dotenv()

    #Get API Key from env variable
    api_key = os.getenv("GROQ_API_KEY")

    #Create a Groq client
    os.environ["GROQ_API_KEY"] = api_key

    config_file = "server/weather.json"

    print("Initializing Chat.......")

    #Create a MCP Client and agent with memory enabled
    mcp_client = MCPClient.from_config_file(config_file)  
    llm = ChatGroq(model="llama3-70b-8192")  # Recommended replacement


    print(f"TYPE OF mcp_client: {type(mcp_client)}")  # should say <class 'mcp_use.client.MCPClient'>
    print(f"TYPE OF llm: {type(llm)}")


    agent = MCPAgent(client=mcp_client, llm=llm, max_steps=15, memory_enabled=True)


    print("Interacting with the agent.......")

    #Run the agent continuously until the user quits
    while True:
        user_input = input("Enter your message: ")
        if user_input.lower() == "quit":
            print("Quitting...")
            break
        if user_input.lower() == "clear":
            agent.clear_conversation_history()
            print("Conversation history cleared...")
            continue
        if user_input.lower() == "show":
            print(agent.conversation_history)
            continue
        response = await agent.run(user_input)
        print(f"Agent: {response}")
        

if __name__ == "__main__":
    asyncio.run(run_memory_chat())

    
