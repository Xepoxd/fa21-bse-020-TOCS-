FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the Flask app
COPY . .

# Expose port 8000
EXPOSE 8000

# Run the Flask app
CMD ["python", "app.py"]
