# WIPO Trademark Management API

A FastAPI-based application for managing trademark records using the WIPO (World Intellectual Property Organization) API.

## Features

- Complete CRUD operations for trademark records
- Integration with WIPO API
- Async HTTP client for better performance
- Input validation using Pydantic models
- Error handling and logging
- SQLite database for local storage
- Auto-generated API documentation

## Prerequisites

- Python 3.8+
- pip package manager
- WIPO API credentials
- Linux environment

## Installation

1. Update system packages:
```bash
sudo apt-get update
sudo apt-get upgrade
```

2. Install Python and required system packages:
```bash
sudo apt-get install python3.8 python3.8-venv python3-pip
```

3. Create project directory:
```bash
mkdir wipo_api
cd wipo_api
```

4. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

5. Create project structure:
```bash
mkdir -p app/api app/services
touch app/__init__.py app/main.py app/config.py app/models.py app/schemas.py
touch app/api/__init__.py app/api/endpoints.py
touch app/services/__init__.py app/services/wipo_service.py
touch requirements.txt .env
```

6. Copy the code files from the codebase to their respective locations in the project structure.

7. Install required packages:
```bash
pip install -r requirements.txt
```

## Configuration

1. Create .env file with your WIPO API credentials:
```bash
nano .env
```

2. Add the following content (replace with your actual credentials):
```
WIPO_API_KEY=your_wipo_api_key
WIPO_API_SECRET=your_wipo_api_secret
DATABASE_URL=sqlite:///./trademarks.db
```

## Running the Application

1. Start the FastAPI server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

2. Access the API:
- API endpoints: `http://localhost:8000/api/v1/`
- API documentation: `http://localhost:8000/docs`
- Alternative documentation: `http://localhost:8000/redoc`

## API Usage Examples

### Create a new trademark
```bash
curl -X POST "http://localhost:8000/api/v1/trademarks" \
     -H "Content-Type: application/json" \
     -d '{
           "name": "TechBrand",
           "description": "Technology services",
           "owner": "Tech Company Inc.",
           "classes": [9, 42],
           "country_codes": ["US", "EU"]
         }'
```

### Search for trademarks
```bash
curl "http://localhost:8000/api/v1/trademarks/search?query=TechBrand&year=2023"
```

### Get trademark details
```bash
curl "http://localhost:8000/api/v1/trademarks/{trademark_id}"
```

### Update trademark
```bash
curl -X PUT "http://localhost:8000/api/v1/trademarks/{trademark_id}" \
     -H "Content-Type: application/json" \
     -d '{
           "status": "registered",
           "description": "Updated description"
         }'
```

### Delete trademark
```bash
curl -X DELETE "http://localhost:8000/api/v1/trademarks/{trademark_id}"
```


