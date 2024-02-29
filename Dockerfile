# Dockerfile
FROM python:3.10-slim

# Set a directory for the app
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Make port 80 available to the world outside this container
#EXPOSE 80

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Command to run the application
#CMD ["python", "./run.py"]
CMD ["python", "docker-run.py"]
# Define the command to run MLflow
#CMD ["mlflow", "server", "--host", "0.0.0.0"]