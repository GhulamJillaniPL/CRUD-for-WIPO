from datetime import datetime
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel

class TrademarkStatus(str, Enum):
    PENDING = 'pending'
    REGISTERED = 'registered'
    REJECTED = 'rejected'
    EXPIRED = 'expired'

class Trademark(BaseModel):
    id: str
    name: str
    description: Optional[str]
    registration_date: datetime
    expiration_date: Optional[datetime]
    status: TrademarkStatus
    owner: str
    classes: List[int]  # Nice Classification
    country_codes: List[str]

class TrademarkCreate(BaseModel):
    name: str
    description: Optional[str] = None
    owner: str
    classes: List[int]
    country_codes: List[str]

class TrademarkUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TrademarkStatus] = None
    owner: Optional[str] = None
    classes: Optional[List[int]] = None
    country_codes: Optional[List[str]] = None

