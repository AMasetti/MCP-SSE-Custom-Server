# MCP SSE Custom Server

This repository contains a custom Server-Sent Events (SSE) implementation for the Model Control Protocol (MCP). The server enables real-time, one-way communication from the server to clients using SSE technology.

## Overview

The MCP SSE Custom Server provides a robust foundation for implementing server-sent events in your applications. It's designed to work seamlessly with the Model Control Protocol, enabling efficient streaming of updates and notifications to connected clients.

## Features

- Real-time server-to-client communication
- Event-driven architecture
- Support for multiple concurrent client connections
- Custom event type handling
- Automatic reconnection handling
- Cross-origin resource sharing (CORS) support

## Prerequisites

- Node.js (v14 or higher)
- npm (Node Package Manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/amasetti/MCP-SSE-Custom-Server.git
cd MCP-SSE-Custom-Server
```

2. Install dependencies:
```bash
npm install
```

## Usage

1. Start the server:
```bash
npm start
```

2. Connect to the SSE endpoint from your client application:
```javascript
const eventSource = new EventSource('http://localhost:3000/events');

eventSource.onmessage = (event) => {
    console.log('Received:', event.data);
};

eventSource.onerror = (error) => {
    console.error('EventSource failed:', error);
};
```

## API Endpoints

### GET /events
- Establishes an SSE connection
- Returns: Server-sent events stream
- Content-Type: text/event-stream

## Configuration

The server can be configured through environment variables:

- `PORT`: Server port (default: 3000)
- `CORS_ORIGIN`: Allowed CORS origins (default: *)

## Error Handling

The server implements robust error handling:
- Automatic reconnection for dropped connections
- Error event propagation to clients
- Connection timeout handling

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository.