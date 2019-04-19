from datetime import datetime

from sqlalchemy import Column, Integer, Float, DateTime

from .meta import Base


class CreatedUpdateMixin:
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


class BiosphereAtmosphereRead(Base, CreatedUpdateMixin):
    __tablename__ = 'biosphere_atmosphere_read'
    id = Column(Integer, primary_key=True)
    registered_at = Column(DateTime, nullable=False)

    atmospheric_pressure = Column(Float)
    precipitation = Column(Float)
    air_temperature = Column(Float)

    # soil temperature is measured at different depths
    soil_temperature_at_2_cm_depth = Column(Float)
    soil_temperature_at_5_cm_depth = Column(Float)
    soil_temperature_at_10_cm_depth = Column(Float)
    soil_temperature_at_20_cm_depth = Column(Float)
    soil_temperature_at_50_cm_depth = Column(Float)
