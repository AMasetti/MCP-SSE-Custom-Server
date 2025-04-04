# MCP Server Implementations

This repository includes two implementations of MCP (Message Control Protocol) servers:

1. **FastAPI with SSE** - A web server implementation using FastAPI and Server-Sent Events
2. **Standalone MCP** - A direct stdin/stdout implementation for use with Claude Desktop

## SSE Implementation

The SSE implementation provides a web-based interface to the MCP server using FastAPI and Server-Sent Events for real-time communication.

### Running the SSE Server

```bash
# Using uvicorn directly
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Or using Docker
docker build -t mcp-sse-server .
docker run -p 8000:8000 mcp-sse-server
```

The server will be accessible at `http://localhost:8000`.

## Standalone MCP Implementation

The standalone implementation provides a simple stdin/stdout interface to the MCP server, designed for use with Claude Desktop or similar applications.

### Running the Standalone MCP Server

```bash
# Build and run using Docker
./run_mcp_container.sh

# Or manually
docker build -t mcp/echo -f Dockerfile.mcp .
docker run -i --rm mcp/echo
```

### Configuring Claude Desktop

To add this MCP server to Claude Desktop, add the following to your Claude Desktop configuration file:

```json
{
  "mcpServers": {
    "echo": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "mcp/echo"
      ]
    }
  }
}
```

## MCP Features

Both implementations provide the same MCP functionality:

1. **Resources** - `echo://{message}` - Echo a message as a resource
2. **Tools** - `echo_tool` - Echo a message as a tool
3. **Prompts** - `echo_prompt` - Create an echo prompt

## Project Structure

- `app/main.py` - Main FastAPI application with MCP functionality
- `app/sse.py` - SSE implementation with Starlette for real-time communication
- `app/mcp_server.py` - Standalone MCP server with stdin/stdout interface
- `Dockerfile` - Container configuration for SSE server
- `Dockerfile.mcp` - Container configuration for standalone MCP server
- `run_mcp_container.sh` - Script to build and run the standalone MCP container

## API Endpoints (SSE Implementation)

- `GET /` - Root endpoint returning a simple greeting
- `GET /sse/` - SSE endpoint for establishing real-time connections
- `POST /messages/` - Endpoint for sending messages to connected clients

## Requirements

- Python 3.10+
- MCP >= 0.3.0
- FastAPI (for SSE implementation)
- Uvicorn (for SSE implementation)
- Docker (for containerized deployment)
