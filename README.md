# Simple Flask App with Docker

## Run locally with Python

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000 and http://localhost:5000/health.

## Build and run with Docker

```bash
docker build -t simple-flask-app:latest .
docker run --rm -p 5000:5000 --name simple-flask-app simple-flask-app:latest
```

Open http://localhost:5000 and http://localhost:5000/health.

Stop the container with Ctrl+C if running in the foreground.
