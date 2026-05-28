FROM python:3.11-slim

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv==2026.2.2 \
    && pipenv install --system --deploy --ignore-pipfile \
    || pip install fastapi uvicorn httpx pydantic

COPY apps/station-service/src .

RUN mkdir -p /app/data

CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8000"]