
[![Continuus Integration](https://github.com/kb1907/GithubActions-DockerHub-CICD-Tutorial/actions/workflows/github-docker-cicd.yaml/badge.svg)](https://github.com/kb1907/GithubActions-DockerHub-CICD-Tutorial/actions/workflows/github-docker-cicd.yaml)

# Create an MLOps Pipeline With GitHub and Docker Hub in Minutes

- This repo contains application files for [Create an MLOps Pipeline With GitHub and Docker Hub in Minutes](https://heartbeat.comet.ml/create-an-mlops-pipeline-with-github-and-docker-hub-in-minutes-4a1515b6a551) article.

![dock](https://user-images.githubusercontent.com/51021282/193422115-788fdb65-8861-4206-bd23-8d387a216ae2.png)



🚀 Projet MLOps

📌 Description

Ce projet s'inscrit dans une démarche MLOps visant à automatiser le cycle de vie du machine learning, de l'entraînement au déploiement des modèles. Il met en œuvre des outils modernes pour assurer la reproductibilité, le suivi des expériences et l'intégration continue des modèles.

🏗️ Stack technologique

Le projet utilise plusieurs outils et bibliothèques pour gérer l’ensemble du pipeline machine learning :

MLflow : suivi des expériences, gestion des modèles et déploiement.
Flask : API légère pour servir les modèles en production.
Scikit-learn : entraînement et évaluation des modèles (RandomForest, etc.).
Jinja2 : génération dynamique des rapports et dashboards.
Virtual Environment (venv/conda) : isolation des dépendances.

📌 Fonctionnalités principales

Tracking des expériences avec MLflow
Entraînement et évaluation d’un modèle de Machine Learning
Versioning et gestion des artefacts
Déploiement local d’un modèle via Flask
Automatisation du pipeline avec CI/CD

📦 Installation

Clonez le repo et installez les dépendances :

bash
Copier
Modifier
git clone https://github.com/ton-repo/mlops-projet.git
cd mlops-projet
pip install -r requirements.txt
Lancez un serveur MLflow local :

bash
Copier
Modifier
mlflow server --host 127.0.0.1 --port 8080

🚀 Utilisation

Entraînement du modèle :
bash
Copier
Modifier
python train.py
Lancement du serveur Flask :
bash
Copier
Modifier
python app.py
📄 License
