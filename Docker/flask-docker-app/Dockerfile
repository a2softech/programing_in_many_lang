# Base image
FROM python:3.12-slim

# Container में काम करने का folder
WORKDIR /app

# Dependencies install करने के लिए file copy करो
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# अब पूरा code copy करो
COPY . .

# Flask का port
EXPOSE 5000

# Default command
CMD ["python", "app.py"]
