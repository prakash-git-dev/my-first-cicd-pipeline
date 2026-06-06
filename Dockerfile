FROM python:3.10-slim

WORKDIR /app


# Install dependencies if needed (we will use a placeholder since our app is small)

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install pytest

COPY app.py .
COPY test_app.py .

COPY . .

CMD ["python", "app.py"]
