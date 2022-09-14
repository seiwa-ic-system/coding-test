import os
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base
from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

POSTGRES_USER = config("POSTGRES_USER", cast=str)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret)
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="db")
POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
POSTGRES_DB = config("POSTGRES_DB", cast=str, default="postgres")

DATABASE_URL = config(
    "DATABASE_URL",
    default=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
            f"{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}",
)
# DBとの接続
echo: bool = False  # 実行されたSQLを表示する
ENGINE = create_engine(DATABASE_URL, encoding="utf-8", echo=echo)

# Sessionの作成 ORM実行時の設定：自動コミットするか、自動反映するか
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)

# modelで使用する
Base = declarative_base()


def main() -> None:
    db = SessionLocal()
    file_path: str = os.path.join(os.path.dirname(__file__), "init_data.sql")
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            db.execute(line)
            db.commit()


if __name__ == "__main__":
    main()
