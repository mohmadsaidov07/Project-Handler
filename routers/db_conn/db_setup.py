from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
from .db_config import settings
from typing import List

sync_engine = create_engine(url=settings.DATABASE_url_psycopg, echo=True)
async_engine = create_async_engine(url=settings.DATABASE_url_asyncpg, echo=True)

sync_session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    cols_amount: int = 100

    def __repr__(self) -> str:
        table_column_names = self.__table__.columns.keys()
        res: List[str] = []
        for idx, col in enumerate(table_column_names):
            if idx < self.cols_amount:
                res.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__}: {', '.join(res)}>"
