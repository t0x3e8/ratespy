# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install Python dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Install rabbitmq
RUN apt-get update && \
    apt-get install -y rabbitmq-server && \
    apt-get install -y cron

# Copy the current directory contents into the container at /code
COPY . /code/

# Run the command to start uWSGI, RabbitMQ, and Celery Beat
CMD ["sh", "-c", "service rabbitmq-server start && uwsgi app.ini && celery -A myapp beat -l info"]
