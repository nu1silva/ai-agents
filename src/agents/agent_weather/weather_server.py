from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("WeatherService")

@mcp.tool()
async def get_weather(city: str) -> str:
    """Fetches the current weather for a given city."""
    # Using a mock/free REST endpoint for demonstration
    url = f"https://wttr.in/{city}?format=3"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        return resp.text.strip()

if __name__ == "__main__":
    mcp.run()