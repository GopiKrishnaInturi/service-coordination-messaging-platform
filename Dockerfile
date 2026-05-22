FROM python:3.11-slim

WORKDIR /coordination

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "runtime:app", "--host", "0.0.0.0", "--port", "8110"]