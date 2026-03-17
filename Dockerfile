# Python image
FROM python:3.11-slim

# code into image
WORKDIR /app

# installing the dependecies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY . .

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]