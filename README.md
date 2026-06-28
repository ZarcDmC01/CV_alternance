# CV Numérique — Jesse Richard · Développeur IA

Application web de CV numérique interactif construite avec **FastAPI** + **Jinja2**, déployable via Docker.

## Stack

- **Backend** : FastAPI (Python 3.11)
- **Templates** : Jinja2
- **Frontend** : HTML / CSS / Vanilla JS
- **Déploiement** : Docker

## Lancer l'application

```bash
# Cloner le dépôt
git clone https://github.com/ZarcDmC01/CV_alternance.git
cd CV_alternance

# Installer les dépendances
pip install -r requirements.txt

# Démarrer le serveur
uvicorn FastAPI_UI:app --reload
```

L'application est accessible sur `http://localhost:8000`.

## Routes

| Route | Description |
|---|---|
| `GET /` | Portfolio interactif complet |
| `GET /cv` | CV format A4 imprimable (→ PDF via navigateur) |
| `GET /health` | Healthcheck |

## Docker

```bash
docker build -t cv-jesse .
docker run -p 8000:8000 cv-jesse
```

## Structure

```
.
├── FastAPI_UI.py          # Application FastAPI
├── requirements.txt
├── Dockerfile
├── templates/
│   ├── index.html         # Portfolio interactif
│   └── cv-print.html      # CV format A4 imprimable
└── static/
    ├── css/style.css
    ├── js/main.js
    └── img/               # (photo.jpg à placer ici)
```

## Auto-watcher (dev)

Pour l'auto-commit/push lors des modifications de `FastAPI_UI.py` :

```bash
pip install watchdog
python .github/workflows/autowatcher.py
```

## Branches

| Branche | Description |
|---|---|
| `main` | Production stable |
| `Jesse` | Développement Jesse — CI → auto-PR |
| `Simo` | Développement Simo — CI → auto-PR |
| `Matthieu` | Développement Matthieu — CI → auto-PR |
