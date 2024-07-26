## コマンド

uvicorn app.main:app --reload

python -m venv venv


### migration

alembic init db
alembic revision --autogenerate
一番最新のものを適用
alembicテーブルに対応するバージョンがあり、最新と一致しているかを定期的に確認
Schemeの追跡とかで使ったりする
alembic upgrade head