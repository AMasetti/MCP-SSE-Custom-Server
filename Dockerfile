# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY app/ app/

# Expose port 8000 so the app is accessible externally
EXPOSE 8000

# Command to run the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]