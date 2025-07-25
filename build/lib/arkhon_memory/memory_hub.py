# arkhon_memory/memoryhub.py
# This module implements the MemoryHub class for managing memory items.
# It provides methods to load, save, append, and query memory items.

import json
import uuid
import os
from datetime import datetime
from typing import List, Optional
from .schemas import MemoryItem
from .decay import compute_score

class MemoryHub:
    def __init__(self, memory_path: str):
        self.path = memory_path
        self.memory: List[MemoryItem] = []
        self.load()

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                data = json.load(f)
                self.memory = [MemoryItem(**item) for item in data]
        else:
            self.memory = []

    def save(self):
        with open(self.path, 'w') as f:
            json.dump([item.dict() for item in self.memory], f, indent=2, default=str)

    def append(self, item: MemoryItem):
        self.memory.append(item)
        self.save()

    def query(self, query_str: str, top_k: int = 5) -> List[MemoryItem]:
        results = []
        for item in self.memory:
            if query_str.lower() in item.content.lower() or any(query_str.lower() in tag for tag in item.tags):
                score = compute_score(item)
                results.append((item, score))
        ranked = sorted(results, key=lambda x: x[1], reverse=True)
        return [item for item, _ in ranked[:top_k]]
