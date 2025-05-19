FROM python:3.12

WORKDIR /app
COPY . /app/

RUN pip install uv
RUN uv pip install --system .