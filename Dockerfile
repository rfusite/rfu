# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install poetry and dependencies
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Collect static files
RUN python manage.py collectstatic --noinput

# Install Gunicorn
RUN pip install gunicorn

# Expose the port the app runs in
EXPOSE 8000

# Define the command to run the app using Gunicorn
CMD ["gunicorn", "rfu.wsgi:application", "--bind", "0.0.0.0:8000"]
