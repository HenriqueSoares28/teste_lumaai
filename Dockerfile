# Usa uma imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que o app usará (ajuste se necessário)
EXPOSE 5000

# Comando para rodar o app
CMD ["python", "app.py"]
