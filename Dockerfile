# Base image
FROM python:3.11

# Set working directory
WORKDIR /usr/src/checkpoint_backend

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all application files
COPY . .

# Expose application port
EXPOSE 8000

# Define default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]