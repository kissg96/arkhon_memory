# Arkhon Memory SDK

**Clean, LOCAL (!!!), long-term memory for autonomous LLM agents and agentic systems.**  
A foundational component built to support persistence, learning, and context recall — without database bloat or framework lock-in.

---

## Contributing & Feedback

I welcome feedback, issues, and pull requests!  
If you find a bug or have ideas for improvement, please open an issue or submit a PR on [GitHub](https://github.com/kissg96/arkhon_memory).

For questions, feature requests, or direct contact:  
**Email:** [kissg@me.com](mailto:kissg@me.com)

Star the repo if you find Arkhon useful or want to follow updates!

---

[![PyPI version](https://img.shields.io/pypi/v/arkhon-memory.svg?style=flat-square)](https://pypi.org/project/arkhon-memory/)
[![Python versions](https://img.shields.io/pypi/pyversions/arkhon-memory.svg?style=flat-square&cacheseconds=0)](https://pypi.org/project/arkhon-memory/)
[![License](https://img.shields.io/github/license/kissg96/arkhon_memory.svg?style=flat-square)](https://github.com/kissg96/arkhon_memory/blob/main/LICENSE)

---

## Install

```bash
pip install arkhon-memory
```
Supports Python 3.8+ and pydantic 2.x.

---

## What is Arkhon Memory?

Most agent “memory” is brittle: chat logs, hacky context, or heavyweight vector DBs.

Who is this for: Indie hackers, researchers, agent devs, and tinkerers, ANYONE tired of vector DBs or lock-in memory “solutions”.

Builders who want cognitive-like, composable memory — not chat history hacks - AND all of it is happening/stored locally not in anyone elses cloud.

**Arkhon** is a *lightweight, composable memory layer*:
- JSON-native, structured, and easy to reason about
- Tracks relevance over time (with time decay + reuse boosting)
- Designed for event-driven, session-aware agent workflows
- No dependencies except Python & [pydantic](https://pydantic.dev/)

> Arkhon is the “active memory” foundation of a much larger system we call Cathedral.  
> This SDK is for builders who want real persistence — and want to keep their stack simple.

---

## Features

- **Plug-and-play**: add persistent memory to any LLM agent in minutes
- **Time decay & reuse**: fresher and more-used facts stay relevant
- **Tagging & snapshots**: organize, search, and summarize memory easily
- **Session lifecycle hooks**: manage memory at start/end of sessions
- **No bloat**: no vector DBs, no LangChain, no black-box magic

---

## License

MIT — free to use, modify, or integrate.

---

## Quick Start (included in examples folder)

```python
from arkhon_memory.memory_hub import MemoryHub
from arkhon_memory.schemas import MemoryItem
from arkhon_memory.lifecycle import on_session_start, on_session_exit
from datetime import datetime

hub = on_session_start("demo_memory.json")
item = MemoryItem(
    content="Tokyo has the world's largest metro population.",
    tags=["geography", "asia"],
    timestamp=datetime.utcnow(),
)
hub.append(item)

results = hub.query("tokyo")
for r in results:
    print("Found:", r.content, r.tags)

on_session_exit(
    hub,
    tags=["demo", "test"],
    summary="Demo session saving basic fact about Tokyo.",
    title="Tokyo Fact Demo"
)

