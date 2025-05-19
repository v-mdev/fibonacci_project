FROM python:3.12

WORKDIR /app
COPY . /app/

RUN uv pip install --system .

ENTRYPOINT ["python", "src/main.py"]