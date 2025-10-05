# HealthTech – Plantilla

## Requisitos
- Node.js 20+
- Python 3.13 + Pipenv
- PostgreSQL 16+ (con pgAdmin o psql)

## Primera vez (tras clonar)
```bash

# Front
cd apps/frontend
npm i
cp .env.example .env
#Para abrir en web
npm run dev / npm run start
Web: http://localhost:5173

(No necesitais Docker si no vais a tocar el back)


# Back

Empezamos con la base de datos:
    Instalamos y abrimos Docker
    En la raíz del repo poner:
    docker compose -f docker-compose.db.yml up -d

Preparamos el back:
    cd apps/backend
    pipenv sync
    pipenv install "psycopg[binary]"
    cp .env.example .env
    #Para abrir en web
    pipenv run start
    API: http://localhost:8000/api/health

# Notas
Si el back te da un Ok al abrirlo tood funciona correctamente.