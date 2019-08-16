from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from lba_data_validator.models.meta import Base


tower_variable_assoc_table = Table('tower_variable_assoc',
                                   Base.metadata,
                                   Column('tower_id', Integer, ForeignKey('Tower.id')),
                                   Column('variable_id', Integer, ForeignKey('Variable.id')))


class Tower(Base):
    """Model a data collecting tower."""
    __tablename__ = 'tower'

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

