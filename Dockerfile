# Start from a lightweight Python base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your local application files into the container
COPY . .

# Install the necessary library
RUN pip install flask

# Set the command to run the application
CMD ["python", "app.py"]