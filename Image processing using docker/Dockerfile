# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Pillow Package
RUN pip install Pillow

# Run pythonscript.py when the container launches
CMD ["python", "./pythonscript.py"]

