FROM python:3.4

# Install Postgres Client
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Cache Dependency Install
ADD ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r ./requirements.txt

# Add Repository
ADD . /app/

# Run Migrations & Server
EXPOSE 8000
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
