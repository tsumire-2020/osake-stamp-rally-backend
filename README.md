## コマンド

uvicorn app.main:app --reload

python -m venv venv


### migration

alembic init db
alembic revision --autogenerate
alembic upgrade head