# MCP SSE Custom Server

A custom server implementation using FastAPI and Server-Sent Events (SSE) with MCP (Message Control Protocol) for real-time communication.

## Overview

This project demonstrates how to build a custom server that:
- Uses FastAPI as the main web framework
- Implements Server-Sent Events (SSE) for real-time communication
- Integrates with MCP for message handling and tool execution
- Includes simple echo functionality as examples

## Requirements

- Python 3.10+
- MCP library
- FastAPI
- Uvicorn

## Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running Locally

Start the server with:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The server will be accessible at `http://localhost:8000`.

### Docker Deployment

Build and run the Docker container:

```bash
docker build -t mcp-sse-server .
docker run -p 8000:8000 mcp-sse-server
```

## Project Structure

- `app/main.py` - Main FastAPI application with MCP functionality
- `app/sse.py` - SSE implementation with Starlette for real-time communication
- `Dockerfile` - Container configuration for deployment

## API Endpoints

- `GET /` - Root endpoint returning a simple greeting
- `GET /sse/` - SSE endpoint for establishing real-time connections
- `POST /messages/` - Endpoint for sending messages to connected clients

## MCP Features

The server implements three types of MCP functionality:

1. **Resources** - `echo://{message}` - Echo a message as a resource
2. **Tools** - `echo_tool` - Echo a message as a tool
3. **Prompts** - `echo_prompt` - Create an echo prompt

## Example Usage

You can test the SSE connection by opening a browser and navigating to the `/sse/` endpoint.

To use the echo tool or resources, send appropriate requests through the MCP protocol.
