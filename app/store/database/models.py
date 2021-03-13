from gino import Gino

from app.store.database.accessor import PostgresAccessor

db = Gino()
database_accessor = PostgresAccessor()