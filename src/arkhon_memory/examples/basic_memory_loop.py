# arkhon_memory/examples/basic_memory_loop.py
# This script demonstrates a basic memory loop using the MemoryHub class.

from arkhon_memory.memory_hub import MemoryHub
from arkhon_memory.schemas import MemoryItem
from arkhon_memory.lifecycle import on_session_start, on_session_exit
from datetime import datetime

# Start a session and load memory
memory_path = "demo_memory.json"
hub = on_session_start(memory_path)

# Append a memory entry
item = MemoryItem(
    content="Tokyo has the world's largest metro population.",
    tags=["geography", "asia"],
    timestamp=datetime.utcnow(),
    reuse_count=0
)
hub.append(item)

# Query for something related
results = hub.query("tokyo")
for r in results:
    print("Found:", r.content, r.tags)

# End session with a snapshot
on_session_exit(
    hub,
    tags=["demo", "test"],
    summary="Demo session saving basic fact about Tokyo.",
    title="Tokyo Fact Demo"
)

print("Session snapshot saved.")
