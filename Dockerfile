FROM nvidia/cuda:12.4.1-base-ubuntu22.04

WORKDIR /app
COPY main.py /app/main.py

CMD ["python3", "/app/main.py"]
