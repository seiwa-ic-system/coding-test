from sqlalchemy import (
    Column,
    Integer,
    String,
)

from load_data import Base


class EAV(Base):

    __tablename__ = "eav"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    e_id = Column(Integer, nullable=False)
    attribute = Column(String(256), nullable=False)
    value = Column(String(256), nullable=False)
