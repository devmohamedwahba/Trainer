FROM python:3.8-slim-buster

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt



RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
COPY entrypont.sh /
ENTRYPOINT ["sh", "/entrypont.sh"]