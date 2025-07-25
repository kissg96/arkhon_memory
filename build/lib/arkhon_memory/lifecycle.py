# arkhon_memory/lifecycle.py
# This module handles session lifecycle events for memory management.
# It provides functions to initialize memory at session start and create snapshots at session exit.

import json
from .memory_hub import MemoryHub
from .schemas import Snapshot
from datetime import datetime

def on_session_start(memory_path: str) -> MemoryHub:
    """Initialize memory at session start."""
    hub = MemoryHub(memory_path)
    return hub

def on_session_exit(hub: MemoryHub, tags=None, summary: str = "", title: str = "Session Snapshot"):
    """Create and save a snapshot at session exit."""
    if tags is None:
        tags = []

    snapshot = Snapshot(
        title=title,
        summary=summary,
        tags=tags,
        timestamp=datetime.utcnow(),
        raw=""  # Could add path to full log if used in your system
    )

    # Optionally, you could save this snapshot somewhere
    snapshot_path = hub.path.replace('.json', '_snapshot.json')
    with open(snapshot_path, 'w') as f:
        f.write(snapshot.json())