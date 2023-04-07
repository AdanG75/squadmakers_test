from sqlalchemy import Column, Integer, DateTime, String, Boolean

from data.local.database import Base


class DBJoke(Base):
    __tablename__ = "jokes"
    id_joke = Column('id_joke', Integer, primary_key=True, index=True)
    joke = Column('joke', String)
    created_time = Column('created_time', DateTime(timezone=False))
    updated_time = Column('updated_time', DateTime(timezone=False))
    dropped = Column('dropped', Boolean)
