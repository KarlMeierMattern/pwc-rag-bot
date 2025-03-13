# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements.txt first to leverage Docker caching
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install PyTorch and related libraries (combine this with the previous RUN statement)
RUN pip install --no-cache-dir torch torchvision torchaudio

# Copy the rest of the application files
COPY . .

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "app.py"]