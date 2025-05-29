from mcp.server.fastmcp import FastMCP
from typing import Any
import httpx


#Iniitializing the MCP server
server = FastMCP("weather")

WEATHER_API_KEY = "8dfe5623caee38382c0b9bd53d80cf93"

city_name = "Austin"

#Defining the weather API endpoint


@server.tool()
def get_weather(city_name: str) -> dict[str, Any]:
    """Get the weather for a given city using coordinates."""
    # Convert city name to coordinates
    geo_url = f"https://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={WEATHER_API_KEY}"
    geo_response = httpx.get(geo_url)
    geo_data = geo_response.json()

    if not geo_data:
        return {"error": "City not found"}

    lat = geo_data[0]['lat']
    lon = geo_data[0]['lon']

    # Fetch weather data using coordinates
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}"
    weather_response = httpx.get(weather_url)
    return weather_response.json()


@server.resource("echo://{message}")
def echo_resource(message: str) -> str:
    """Echo a message as a resource"""
    return f"Resource echo: {message}"








