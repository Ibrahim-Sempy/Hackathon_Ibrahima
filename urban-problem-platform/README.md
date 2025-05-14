# Plateforme de Signalement et de Navigation Urbaine – Guinée

## Prérequis

- Python 3.8+ installé
- [pip](https://pip.pypa.io/en/stable/) installé
- [Git](https://git-scm.com/) (optionnel, si tu clones le projet)
- [PostgreSQL](https://www.postgresql.org/) (optionnel, si tu utilises PostgreSQL)
- Un accès internet pour les dépendances et les CDN (Bootstrap, Chart.js, Leaflet...)

## 1. Récupération du code

Clone le dépôt ou copie les fichiers sur la nouvelle machine :


git clone <url-du-depot>
cd urban-problem-platform


## 2. Création et activation d’un environnement virtuel


python -m venv venv
# Sous Windows
venv\Scripts\activate
# Sous Mac/Linux
# source venv/bin/activate

## 3. Installation des dépendances


pip install -r requirements.txt


Si tu n’as pas de fichier `requirements.txt`, crée-le avec :


Django>=4.2
Pillow


Et installe :


pip install Django Pillow


## 4. Configuration de la base de données

Par défaut, le projet utilise SQLite (aucune config requise).  
Si tu utilises PostgreSQL, configure `DATABASES` dans `urban-problem-platform/settings.py`.

## 5. Application des migrations


python manage.py migrate


## 6. Création d’un superutilisateur (admin)


python manage.py createsuperuser

Suis les instructions pour définir un nom d’utilisateur, un email et un mot de passe.

## 7. Collecte des fichiers statiques (optionnel en dev)


python manage.py collectstatic

## 8. Lancement du serveur de développement


python manage.py runserver


## 9. Accès à l’application

- **Page d’accueil/inscription** : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Connexion** : [http://127.0.0.1:8000/accounts/login/](http://127.0.0.1:8000/accounts/login/)
- **Tableau de bord admin signalements** : [http://127.0.0.1:8000/reports/admin/](http://127.0.0.1:8000/reports/admin/) (réservé aux administrateurs)
- **Admin Django** : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 10. Téléversement de fichiers (photos)

Assure-toi que le dossier `media/` existe à la racine du projet et que tu as les droits d’écriture.

## 11. Configuration email (pour la production)

Configure les paramètres email dans `settings.py` pour l’envoi de mails (confirmation, notifications…).

## 12. (Optionnel) Déploiement

Pour un déploiement en production, configure :
- Un serveur web (Nginx, Apache)
- Un serveur WSGI (Gunicorn, uWSGI)
- Un domaine et HTTPS
- Les variables d’environnement (SECRET_KEY, DEBUG, etc.)



## Fonctionnalités principales

- Inscription/connexion sécurisée
- Signalement de problèmes urbains (avec photo, géolocalisation)
- Consultation et filtrage des signalements sur carte et tableau
- Tableau de bord administrateur avec gestion des statuts et statistiques (diagramme en cercle)
- Gestion des routes et points d’intérêt
- Interface différenciée utilisateur/admin



## Structure du projet


urban-problem-platform/
│
├── accounts/
├── navigation/
├── reports/
├── templates/
│   ├── base.html
│   ├── registration/
│   ├── navigation/
│   └── reports/
├── media/
├── manage.py
└── requirements.txt




## Conseils

- Pour tester les fonctionnalités admin, connecte-toi avec un compte superutilisateur.
- Pour ajouter des signalements, utilise le formulaire prévu dans l’interface.
- Pour toute erreur, consulte la console ou les logs Django.


**Bonne utilisation de la plateforme !**