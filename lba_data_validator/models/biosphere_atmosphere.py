from sqlalchemy import Column, Integer, DateTime, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from lba_data_validator.models.mixin import CreatedUpdatedMixin
from .meta import Base


class BiosphereAtmosphereVariable(Base):

    __tablename__ = 'biosphere_atmosphere_variable'

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    minimum_value = Column(Numeric)
    maximum_value = Column(Numeric)

    def __repl__(self):
        return self.name


class BiosphereAtmosphereRead(Base, CreatedUpdatedMixin):

    __tablename__ = 'biosphere_atmosphere_read'

    id = Column(Integer, primary_key=True)

    variable_id = Column(Integer, ForeignKey('biosphere_atmosphere_variable.id'), nullable=False)
    variable = relationship('BiosphereAtmosphereVariable')

    registered_value = Column(Numeric, nullable=False)
    registered_at = Column(DateTime, nullable=False)
