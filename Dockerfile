# Build stage
FROM python:3.9-slim-bullseye as build-stage
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.9-slim-bullseye
WORKDIR /app
COPY --from=build-stage /app /app
COPY . .
CMD ["python", "app.py"]
# # Use an official Python runtime as a parent image
# FROM python:3.9

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Make port 8888 available to the world outside this container
# EXPOSE 8888
# # Run app.py when the container launches
# CMD ["python", "app.py"]