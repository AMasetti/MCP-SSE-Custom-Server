# MCP Server Implementations

The Model Context Protocol (MCP) serves as an open standard to facilitate communication between language models and client applications. Its modular architecture allows developers to build, deploy, and interact with servers that can manage context, data streams, and event-based communications. This openness has spurred a community effort to create accessible, scalable, and secure solutions that bridge various platforms and frameworks.

This repository includes two implementations of MCP (Message Control Protocol) servers:

1. **FastAPI with SSE** - A web server implementation using FastAPI and Server-Sent Events
2. **Standalone MCP** - A direct stdin/stdout implementation for use with Docker Containers


## MCP Features

Both implementations provide the following MCP functionality:

1. **Resources**
   - `echo://{message}` - Echo a message as a resource

2. **Tools**
   - `echo_tool` - Echo a message as a tool
   - `demo_tool` - Demonstrate tool functionality by adding two numbers

3. **Prompts**
   - `echo_prompt` - Create an echo prompt

## Getting Started

### Prerequisites

- Python 3.10+
- MCP >= 0.3.0
- Docker (for containerized deployment)
- FastAPI and Uvicorn (for SSE implementation)

### Installation

Clone this repository and navigate to the project directory:

```bash
git clone git@github.com:AMasetti/MCP-SSE-Custom-Server.git
cd mcp-server-implementations
```

## SSE Implementation

The SSE (Server-Sent Events) implementation provides real-time data streaming capabilities over HTTP. This is particularly useful for streaming responses from AI models.

### Building and Running

You can run the SSE server using either Docker or directly with uvicorn:

```bash
# Using Docker
make build-sse
make run-sse

# Or using uvicorn directly
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The server will be accessible at `http://localhost:8000`.

### Configuring Claude Desktop

To add the SSE server to Claude Desktop, add the following to your configuration file:

```json
{
  "mcpServers": {
    "example-sse": {
      "url": "http://localhost:8000/sse",
      "env": {}
    }
  }
}
```

## Standalone MCP Implementation

The standalone implementation provides a simple stdin/stdout interface, making it ideal for direct integration with Claude Desktop or similar applications.

### Building and Running

```bash
# Using Make commands
make build-local
make run-local

# Or using Docker directly
docker build -t mcp/echo -f Dockerfile.mcp .
docker run -i --rm mcp/echo
```

### Configuring Claude Desktop

Add the following to your Claude Desktop configuration file:

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

## Project Structure

```
.
├── app/
│   ├── mcp_server.py    # Core MCP server implementation
│   └── sse.py           # SSE implementation with Starlette
├── Dockerfile.mcp       # Container config for standalone MCP
├── Dockerfile.sse       # Container config for SSE server
└── Makefile            # Build and run commands
```

## API Endpoints (SSE Implementation)

- `GET /` - Root endpoint returning a simple greeting
- `GET /sse/` - SSE endpoint for establishing real-time connections
- `POST /messages/` - Endpoint for sending messages to connected clients

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
