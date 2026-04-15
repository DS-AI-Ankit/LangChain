from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """
    get the weather details of the location.
    """
    return "It is raining in New Delhi"

if __name__=="__main__":
    mcp.run(transport="streamable-http")
