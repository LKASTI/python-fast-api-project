"""
fields:
- energy_kwh: float | the energy reading at the timestamp and for the meter
- timestamp: str/datetime | the time when the energy was read for a meter
- meter_id: str | the meter identifier

Questions:
- Is it valid to have two readings with the same timestamp, and meter_id but with different energy_kwh values?
    - assume invalid
- How should we compare readings?
    - energy_kwh values
"""
from datetime import datetime
from dataclasses import dataclass
from pydantic import BaseModel, Field


@dataclass(frozen=True)
class EnergyReadingDataclass:
    energy_kwh: float
    meter_id: str
    timestamp: datetime


@dataclass(frozen=True)
class EnergyReadingDataclassWithValidation:
    energy_kwh: float
    meter_id: str
    timestamp: datetime

    def __post_init__(self):
        if self.energy_kwh is None or (not isinstance(self.energy_kwh, float)):
            raise ValueError('energy_kwh cannot be empty and must be a float')
        if not self.meter_id or (not isinstance(self.meter_id, str)):
            raise ValueError('meter_id cannot be empty and must be a str')
        if not self.timestamp or (not isinstance(self.timestamp, datetime)):
            raise ValueError('timestamp cannot be empty and must be a datetime')
        if self.timestamp.tzinfo is None or self.timestamp.utcoffset() is None:
            raise ValueError("timestamp must be timezone-aware")

class EnergyReadingPydantic(BaseModel):
    energy_kwh: float = Field(ge=0.0)
    meter_id: str
    timestamp: datetime

    # use default_factory() for mutables (lists, dicts)