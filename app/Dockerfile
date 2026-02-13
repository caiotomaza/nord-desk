# app/Dockerfile
FROM python:3.11-slim

# Define variáveis de ambiente para evitar arquivos .pyc e logs em buffer
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instala dependências do sistema necessárias para o Postgres
RUN apt-get update && apt-get install -y libpq-dev gcc

# Instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o projeto
COPY . .

# Comando padrão (pode ser sobrescrito pelo docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]