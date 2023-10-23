# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python function and Flask app
COPY function.py .
COPY app.py .

# Expose port 5000 for Flask app
EXPOSE 8080

# Define the command to run your Flask app inside the container
CMD ["python", "app.py"]