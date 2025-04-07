build-sse:
	docker build -t mcp-sse-server -f Dockerfile.sse .

build-local:
	docker build -t mcp-local-server -f Dockerfile.mcp .

run-sse:
	docker run -d -p 8000:8000 mcp-sse-server

run-local:
	docker run -d -p 8000:8000 mcp-local-server

