# projeto-computa-o-libras
Projeto de Computação I

criar migration:
docker-compose exec web alembic revision --autogenerate -m "add lesson table"

aplicar migrations:
docker-compose exec web alembic upgrade head

entrar no banco:
docker-compose exec db psql --username=postgres --dbname=postgres