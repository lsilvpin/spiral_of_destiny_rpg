
FROM mcr.microsoft.com/devcontainers/python:3.11

WORKDIR /app
ADD . /app/
EXPOSE 8000

RUN apt upgrade -y
RUN apt update -y
RUN pip install --upgrade pip

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# RUN pip install -r requirements.txt
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
