import asyncio
import os
import sys
from pathlib import Path
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    try:
        # 1. Initialize Llama 3.1 (supports tool calling)
        llm = ChatOllama(model="llama3.1", temperature=0)

        # 2. Get the absolute path to weather_server.py (in the same directory)
        current_dir = Path(__file__).parent
        weather_server_path = str(current_dir / "weather_server.py")
        
        # Get the python executable from the virtual environment
        python_executable = sys.executable
        
        # 3. Connect to your MCP Server
        client = MultiServerMCPClient({
            "weather": {
                "command": python_executable,
                "args": [weather_server_path],
                "transport": "stdio"
            }
        })
        
        # 4. Pull tools from the MCP server
        tools = await client.get_tools()
        print(f"Loaded tools: {[tool.name for tool in tools]}")

        # 5. Create the agent with tools
        agent = create_agent(
            model=llm,
            tools=tools,
            system_prompt="You are a helpful assistant that can use tools to answer questions."
        )

        # 6. Run the agent
        response = await agent.ainvoke({
            "messages": [{"role": "user", "content": "What is the weather like in Almere right now?"}]
        })
        
        # Print the final answer
        print(f"\nFinal Answer: {response['messages'][-1].content}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())