FROM python:3.5-alpine3.7

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

WORKDIR /app/CaptureArchive/

ENTRYPOINT [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]