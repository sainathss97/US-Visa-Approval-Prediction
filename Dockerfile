# Use official Python image as base
FROM python:3.8.5-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements file
# COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# # Copy application code
# COPY . .

# # Expose port (change if your app uses a different port)
# EXPOSE 8080

# Command to run the application (change app.py to your entrypoint)
CMD ["python", "app.py"]