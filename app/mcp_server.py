from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP
from app.sse import create_sse_server
import os
import logging
import sys
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP instance
mcp = FastMCP("Echo")

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

@mcp.tool()
def calculate_ngrams(text: str, n: int = 2, level: str = "word") -> List[str]:
    """
    Calculate n-grams for the given string.

    Args:
        text: The input text to generate n-grams from
        n: Size of the n-gram (default: 2)
        level: Type of n-grams to generate: "word" or "character" (default: "word")

    Returns:
        A list of n-gram strings
    """
    if n < 1:
        return ["Error: n must be a positive integer"]

    if level.lower() not in ["word", "character"]:
        return ["Error: level must be either 'word' or 'character'"]

    if level.lower() == "word":
        # Split the text into words
        tokens = text.split()
    else:  # character level
        # Use each character as a token
        tokens = list(text)

    # Handle edge case: if text is shorter than n tokens
    if len(tokens) < n:
        return [' '.join(tokens) if level.lower() == "word" else ''.join(tokens)]

    # Generate n-grams
    ngrams = []
    for i in range(len(tokens) - n + 1):
        if level.lower() == "word":
            ngram = ' '.join(tokens[i:i+n])
        else:  # character level
            ngram = ''.join(tokens[i:i+n])
        ngrams.append(ngram)

    return ngrams

@mcp.prompt()
def echo_prompt(message: str) -> str:
    """Create an echo prompt"""
    return f"Please process this message: {message}"

def create_app():
    """Create either a FastAPI app for SSE or return the MCP instance based on SERVER_TYPE"""
    server_type = os.getenv("SERVER_TYPE", "local").lower()

    if server_type == "sse":
        app = FastAPI()
        # Mount the Starlette SSE server onto the FastAPI app
        app.mount("/", create_sse_server(mcp))
        return app
    elif server_type == "local":
        return mcp
    else:
        raise ValueError(f"Invalid SERVER_TYPE: {server_type}. Must be either 'sse' or 'local'")

app = create_app()

if __name__ == "__main__":
    if isinstance(app, FastMCP):
        logger.info("Running Local MCP server")
        app.run()
    else:
        logger.info("Running FastAPI MCP Server")
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)