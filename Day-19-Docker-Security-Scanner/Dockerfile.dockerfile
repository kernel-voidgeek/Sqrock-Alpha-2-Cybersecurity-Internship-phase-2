
FROM python:latest

WORKDIR /app

COPY . .

EXPOSE 22
EXPOSE 8080

CMD ["python", "app.py"]
