## Command

uvicorn main:app --reload
uvicorn app.main:app --reload

## dumpしてデータを入れるケースを手順を用意する

- [] マイグレーションシステムを導入する
alembic init db
alembic revision --autogenerate
alembic upgrade head

```
import main
target_metadata = main.Base.metadata
from main import Todo
```

- [] dumpデータを格納する#   o s a k e - s t a m p - r a l l y - b a c k e n d  
 