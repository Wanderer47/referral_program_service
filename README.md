# Referral program service.

---

Start test postgres DB

Run postgres DB in docker container:
```
docker run --rm -d --name postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 postgres
docker exec -it postgres psql -U postgres -c 'CREATE DATABASE postgres;'
```

Initialize Alembic to project:
```alembic init migrations```

Autogenerate migrations:
```alembic revision --autogenerate -m "Create a baseline migrations"```

Execute the migration on the database:
```alembic upgrade head```

---
