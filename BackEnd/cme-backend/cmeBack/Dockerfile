# Usar uma imagem base oficial do Python
FROM python:3.10-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instalar as dependências necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código do projeto para o diretório de trabalho
COPY . .

# Expor a porta que o Django usará (geralmente 8000)
EXPOSE 8000

# Definir a variável de ambiente para desativar o buffering de saída do Python
ENV PYTHONUNBUFFERED=1

# Comando para rodar as migrações e iniciar o servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
