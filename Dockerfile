# Utiliser l'image de base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Commande par défaut à exécuter
CMD ["python", "app.py"]
