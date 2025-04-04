# MCP Stack

This Docker Compose setup provides a convenient way to run the MCP (Model Control Protocol) services in a unified stack.

## Services

The MCP Stack includes the following services:

1. **github-mcp**: GitHub MCP service that requires a GitHub Personal Access Token
2. **echo-sse**: Echo SSE service that runs with FastAPI/Uvicorn on port 8000
3. **echo-local**: Echo Local service that runs in interactive mode

## Prerequisites

- Docker and Docker Compose installed on your system
- GitHub Personal Access Token (for the github-mcp service)

## Getting Started

1. Clone this repository
2. Set your GitHub token as an environment variable:

   ```bash
   export GITHUB_PERSONAL_ACCESS_TOKEN=your_github_token_here
   ```

3. Run the stack:

   ```bash
   docker-compose up --build
   ```

   Use `-d` flag to run in detached mode:

   ```bash
   docker-compose up --build -d
   ```

## Individual Services

You can also run individual services:

```bash
# Run only the GitHub MCP service
docker-compose up github-mcp

# Run only the Echo SSE service
docker-compose up echo-sse

# Run only the Echo Local service
docker-compose up echo-local
```

## Accessing the Services

- **echo-sse**: Available at http://localhost:8000
- **github-mcp** and **echo-local**: These are interactive services that don't expose web endpoints

## Claude Desktop Configuration

To add the MCP services to Claude Desktop, modify your configuration:

```json
{
  "mcpServers": {
    "github": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "GITHUB_PERSONAL_ACCESS_TOKEN",
        "mcp/github"
      ]
    },
    "echo-sse": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "mcp/echo-sse"
      ]
    },
    "echo-local": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "mcp/echo-local"
      ]
    }
  }
}
```