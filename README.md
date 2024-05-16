# FastAPI User Management System

Ce projet est une API de gestion des utilisateurs construite avec FastAPI. Elle permet de créer des utilisateurs, de récupérer des informations sur un utilisateur spécifique, et de lister tous les utilisateurs.

## Installation

Pour récupérer et démarrer ce projet, suivez les instructions ci-dessous.

### Prérequis

- Python 3.8+
- pip

### Récupération du Projet

Clonez le dépôt 

### Création et Activation de l'Environnement Virtuel

Créez un environnement virtuel pour le projet :

```bash
python -m venv venv
```

Activez l'environnement virtuel :

Sur Windows :

```bash
.\venv\Scripts\activate
```
Sur macOS et Linux :

```bash
source venv/bin/activate
```

### Installation des Dépendances

Installez toutes les dépendances requises en exécutant :

```bash
pip install -r requirements.txt
```

### Démarrage de l'API

Lancez le serveur FastAPI avec la commande suivante :

```bash
uvicorn app.main:app --reload
```

Le serveur sera accessible à l'adresse http://localhost:8000.

## Routes API

### Création d'un Utilisateur

URL : /user
Méthode : POST
Données requises :

```json
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "password": "password123"
}
```

Réponse :

```json
{
    "message": "User created successfully"
}
```
Si l'utilisateur existe déjà :

```json
{
    "message": "User already exists"
}
```

### Récupérer un Utilisateur par ID
URL : /user/:id
Méthode : GET
Réponse :

```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```

Si l'utilisateur n'est pas trouvé :

```json
{
    "detail": "User not found"
}
```

### Lister Tous les Utilisateurs
URL : /users
Méthode : GET
Réponse :
```json
[
    {
        "id": 1,
        "name": "John Doe"
    },
    {
        "id": 2,
        "name": "Jane Doe"
    }
]
```