# Use official Python image as base
FROM python:3.8.5-slim-buster

# Set working directory
WORKDIR /app

# # Copy application code with requirements
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Command to run the application (change app.py to your entrypoint)
CMD ["python", "app.py"]