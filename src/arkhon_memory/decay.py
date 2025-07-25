# arkhon_memory/decay.py
# This module implements decay functions for memory items.
# It provides a way to compute scores based on item age and reuse count. Change these parameters to adjust decay behavior or reuse boost.

from datetime import datetime
from math import exp
from typing import Optional
from .schemas import MemoryItem

# Constants — adjust these to change decay behavior
HALF_LIFE_DAYS = 7.0
REUSE_BOOST_WEIGHT = 0.2

def compute_score(item: MemoryItem, now: Optional[datetime] = None) -> float:
    if now is None:
        now = datetime.utcnow()

    age_days = (now - item.timestamp).total_seconds() / 86400
    decay_factor = 0.5 ** (age_days / HALF_LIFE_DAYS)
    reuse_boost = REUSE_BOOST_WEIGHT * item.reuse_count

    return decay_factor + reuse_boost
