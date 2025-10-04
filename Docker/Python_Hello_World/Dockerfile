# Base image (Python ka official image use karenge)
FROM python:3.12-slim

# Container ke andar ek working directory banao
WORKDIR /app

# main.py ko container ke andar copy karo
COPY main.py .

# Container run hone par ye command chalegi
CMD ["python", "main.py"]
