from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from lba_data_validator.models.meta import Base
from lba_data_validator.models.mixin import CreatedUpdatedMixin


class Instrument(Base, CreatedUpdatedMixin):
    __tablename__ = 'instrument'

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    reading_id = Column(Integer, ForeignKey('biosphere_atmosphere_read.id'))
    readings = relationship('BiosphereAtmosphereRead')

    tower_id = Column(Integer, ForeignKey('tower.id'))
    tower = relationship('Tower', back_populates='instruments')
