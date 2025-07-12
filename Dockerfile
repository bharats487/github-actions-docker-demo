# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the application file
COPY app.py .

# Make the script executable
RUN chmod +x app.py

# Set the default command
CMD ["python", "app.py"] 