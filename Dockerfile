FROM python:3.9

WORKDIR /app

COPY app.py .
COPY requirements.txt .
COPY templates/ templates/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]


