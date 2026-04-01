# Calculator API

A simple REST API built with **FastAPI** that provides basic arithmetic operations.

## Features

- ✨ Fast and lightweight REST API
- 🧮 Basic arithmetic operations: Add, Subtract, Multiply
- 📝 Full test coverage with pytest
- 🐳 Docker support for easy deployment
- 📚 Interactive API documentation (Swagger UI)

## Project Structure

```
.
├── main.py           # FastAPI application with all endpoints
├── test_main.py      # Unit tests for all endpoints
├── requirements.txt  # Python dependencies
├── Dockerfile        # Docker configuration
└── README.md         # This file
```

## Requirements

- Python 3.11+
- FastAPI
- Uvicorn
- Pytest
- Httpx

## Installation

### Local Setup

1. Clone or navigate to the project directory:
```bash
cd Calculator
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Server

Start the development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### API Endpoints

#### 1. Home Endpoint
**GET** `/`
```bash
curl http://localhost:8000/
```
**Response:**
```json
{
  "message": "Hello, World!"
}
```

#### 2. Add Two Numbers
**GET** `/add?a=<number1>&b=<number2>`
```bash
curl "http://localhost:8000/add?a=3&b=5"
```
**Response:**
```json
{
  "result": 8
}
```

#### 3. Subtract Two Numbers
**GET** `/subtract?a=<number1>&b=<number2>`
```bash
curl "http://localhost:8000/subtract?a=10&b=4"
```
**Response:**
```json
{
  "result": 6
}
```

#### 4. Multiply Two Numbers
**GET** `/multiply?a=<number1>&b=<number2>`
```bash
curl "http://localhost:8000/multiply?a=4&b=3"
```
**Response:**
```json
{
  "result": 12
}
```

### Interactive Documentation

FastAPI automatically generates interactive API documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Testing

Run the test suite using pytest:
```bash
pytest test_main.py
```

### Test Coverage

The project includes 5 comprehensive tests:
- ✅ Home endpoint returns correct message
- ✅ Addition of positive numbers
- ✅ Subtraction
- ✅ Multiplication
- ✅ Addition with negative numbers

## Docker

### Building the Docker Image

```bash
docker build -t calculator-api .
```

### Running in Docker

```bash
docker run -p 8000:8000 calculator-api
```

The API will be available at `http://localhost:8000`

## Example Usage with Python

```python
import requests

# Add two numbers
response = requests.get("http://localhost:8000/add?a=10&b=5")
print(response.json())  # {'result': 15}

# Subtract two numbers
response = requests.get("http://localhost:8000/subtract?a=10&b=3")
print(response.json())  # {'result': 7}

# Multiply two numbers
response = requests.get("http://localhost:8000/multiply?a=6&b=7")
print(response.json())  # {'result': 42}
```

## API Parameters

All arithmetic endpoints accept two integer parameters:

| Parameter | Type | Description |
|-----------|------|-------------|
| `a` | integer | First number |
| `b` | integer | Second number |

## License

This project is open source and available for educational purposes.

## Author

Created as a sample Calculator API project.
