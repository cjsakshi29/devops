# Use the official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your Python file into the container
COPY calculator.py .

# Run the calculator script
CMD ["python", "calculator.py"]

