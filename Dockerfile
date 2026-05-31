FROM python:3.10-slim

WORKDIR /app

# Install dependencies if needed (we will use a placeholder since our app is small)
RUN pip install pytest

COPY app.py .
COPY test_app.py .

CMD ["python", "app.py"]
