# Using Docker Compose

When you use Docker Compose, you typically do not need to run docker build manually. Instead, you can use the following command:

- <code>docker-compose build</code>  
  Builds the images for the services defined in your docker-compose.yml file. If you have made changes to your docker-compose.yml file or the application code, running this command ensures that the latest version of the image is built.
- <code>docker-compose up</code>  
  Starts the services defined in your docker-compose.yml file. Creates and starts the containers based on the images built in the previous step (or existing images if no changes were made). If the containers are already running, it will restart them.  
   OR, use the below which combines the above lines:
- <code>docker-compose up --build</code>

# Building a single Docker image

If you want to build a single Docker image without using Docker Compose, you would use a Dockerfile along with the commands below. This is useful for testing or when you only have one service to build.

- <code>docker build -t my-streamlit-app .</code>
- <code>docker run -p 8501:8501 my-streamlit-app</code>
