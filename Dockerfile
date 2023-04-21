FROM python:3.11-slim-buster

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


# Create a group and user to run our app
ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}

RUN apt update && apt install -y libmagic1 libpq5

# Install pip requirements
RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY ./app /app

# Change to a non-root user
USER ${APP_USER}:${APP_USER}

CMD ["sh", "-c", "python manage.py wait_for_db && gunicorn project.wsgi:application -c gunicorn.conf.py"]
