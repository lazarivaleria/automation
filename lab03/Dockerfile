
FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Chisinau
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    cron \
    tzdata \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY currency_exchange_rate.py /app/currency_exchange_rate.py
COPY cronjob /app/cronjob
COPY entrypoint.sh /app/entrypoint.sh

# Instalez biblioteca folosita de scriptul laboratorului 02.
RUN pip install --no-cache-dir requests

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
