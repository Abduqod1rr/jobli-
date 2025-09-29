# Python  
FROM python:3.12-slim 

# Workdir
WORKDIR /app

# Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Project files
COPY . .

# Static filesni collect qilish
RUN python manage.py collectstatic --noinput

# Django run
CMD ["gunicorn", "jobli.wsgi:application", "--bind", "0.0.0.0:8000"]
