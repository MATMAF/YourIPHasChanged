FROM python:3.11.4-slim

ENV EMAIL_RECEIVER=email@example.com
ENV SLEEP_TIME=150

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app/
COPY config.py /app/

CMD ["python", "app.py"]
