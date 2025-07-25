# arkhon_memory/schemas.py
# This module defines the schemas used in the memory system. Extend it as needed.
# Using Pydantic for data validation and serialization.

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class MemoryItem(BaseModel):
    content: str
    tags: List[str] = []
    timestamp: datetime
    reuse_count: int = 0

class Snapshot(BaseModel):
    title: str
    summary: str
    tags: List[str] = []
    timestamp: datetime
    raw: Optional[str] = None  # Path or blob, optional
