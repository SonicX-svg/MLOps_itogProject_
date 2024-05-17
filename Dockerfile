FROM ubuntu:24.04           


 
# Copy this repo to a folder in the Docker container
COPY . /app
 
# Set the work directory
WORKDIR /app
 
# Install all the required packages
RUN pip install -r requirements.txt 
