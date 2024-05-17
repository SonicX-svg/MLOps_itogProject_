FROM python:3.10.5-slim-buster


 
# Copy this repo to a folder in the Docker container
COPY . /app
 
# Set the work directory
WORKDIR /app
 
# Install all the required packages
RUN pip install -r requirements.txt 
