FROM python:3.9-slim

# Set an environment variable to store where the app is installed to inside the docker image
WORKDIR /usr/src/app

# Copy the current directory contents (your Flask app) into the container at /usr/src/app
COPY . /usr/src/app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV FLASK_APP=proxy.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run your_flask_app_filename.py when the container launches
CMD ["flask", "run", "--port=80"]