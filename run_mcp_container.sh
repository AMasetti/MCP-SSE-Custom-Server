#!/bin/bash

# Build the Docker image
echo "Building the MCP Docker image..."
docker build -t mcp/echo -f Dockerfile.mcp .

# Run the container with interactive mode to allow stdin/stdout communication
echo "Running the container with stdin/stdout..."
echo "Press Ctrl+C to exit when done testing"
docker run -i --rm mcp/echo

# Example usage from claude_desktop_config.json would be:
# {
#   "mcpServers": {
#     "echo": {
#       "command": "docker",
#       "args": [
#         "run",
#         "-i",
#         "--rm",
#         "mcp/echo"
#       ]
#     }
#   }
# }

echo ""
echo "To add this MCP server to Claude desktop, add the following to your config:"
echo ""
cat sample_claude_config.json