# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages 
RUN pip install requests
RUN pip install rdflib




# Make the script executable
RUN chmod +x grafo.py

# Define the command to run your script when the container starts
CMD ["python", "grafo.py"]