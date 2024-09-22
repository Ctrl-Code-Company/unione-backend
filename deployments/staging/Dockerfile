# Pull base image

FROM python:3.11

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 \
    &&  apt-get install -y ffmpeg
# Set some env varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY /requirements /app
RUN pip install --upgrade pip && pip install --no-cache-dir -r /app/staging.txt
# Add entrypoint.sh
COPY /deployments/staging/entrypoint.sh /app/entrypoint.sh


RUN chmod +x /app/entrypoint.sh
# Copy project
COPY src /app
# Run server
CMD ["/app/entrypoint.sh"]