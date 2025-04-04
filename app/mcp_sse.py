from fastapi import FastAPI
from app.sse import create_sse_server
from mcp.server.fastmcp import FastMCP

app = FastAPI()
mcp = FastMCP("Echo")

# Mount the Starlette SSE server onto the FastAPI app
app.mount("/", create_sse_server(mcp))


@app.get("/")
def read_root():
    return {"Hello": "World"}


# Add MCP functionality with decorators
@mcp.resource("echo://{message}")
def echo_resource(message: str) -> str:
    """Echo a message as a resource"""
    return f"Resource echo: {message}"


@mcp.tool()
def echo_tool(message: str) -> str:
    """Echo a message as a tool"""
    return f"Tool echo: {message}"

@mcp.tool()
def demo_tool(num1: int, num2: int) -> str:
    """Demo a tool"""
    sum = num1 + num2
    return f"The sum of {num1} and {num2} is {sum}"


@mcp.prompt()
def echo_prompt(message: str) -> str:
    """Create an echo prompt"""
    return f"Please process this message: {message}"
