# Use the official Python base image
FROM python:3.9-slim

# create user
RUN useradd -d /home/giga -m -s /bin/bash giga
USER giga

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY app.py .

# Expose the port on which the application will run
EXPOSE 3000

# Set the command to run the application
CMD ["python", "app.py"]
