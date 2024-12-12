# Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /mnt/AAAASTARK/work/python/

# Copy the current directory contents into the container
COPY . .

# Command to run the Python script
CMD ["python", "demo.py"]
