from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
import asyncio

async def main():
    client=MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mathserver.py"],
                "transport":"stdio",
            },
            
            "weather":{
                "transport":"http",
               "url":"http://localhost:8000/mcp",
                

                }
            
        }
    )
    import os
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
    tools=await client.get_tools()                      
    model=ChatGroq(model="llama-3.1-8b-instant")
    agent=create_agent(model,tools)

    # #math_response=await agent.ainvoke(
    #     {"messages":[{"role":"user","content":"What is (3+5+9*2)"}]}
    #     )

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in New Delhi?"}]}
        )

    #print(math_response["messages"][-1].content)
    print(weather_response['messages'][-1].content)

asyncio.run(main())