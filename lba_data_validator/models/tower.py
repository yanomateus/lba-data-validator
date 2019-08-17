from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from lba_data_validator.models.meta import Base


class Tower(Base):
    """Model a data collecting tower."""
    __tablename__ = 'tower'

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    instruments = relationship('Instrument', back_populates='tower')
