# AI Memory Simulator

## Overview

AI Memory Simulator is a terminal-based Python application that mimics how an AI assistant stores, recalls, prioritizes, and forgets information.

Users can save memories with different priority levels, search them using keywords, monitor recall frequency, automatically remove unused memories, and maintain persistent storage using JSON.

The project demonstrates a simplified memory management system inspired by conversational AI assistants.

---

## Features

- Add Memory
- Recall Memory by Keyword
- Priority Levels (High, Medium, Low)
- Recall Counter
- Forget Memory
- Important Memory View
- Memory Statistics
- Automatic Cleanup
- JSON Storage

---

## Project Structure

ai-memory-simulator/

├── memory_engine.py

├── memory_console.py

├── README.md

└── .gitignore

---

## Requirements

Python 3.x

No external libraries required.

---

## Run

```bash
python memory_console.py
```

---

## Menu

```
1. Add Memory
2. View All Memories
3. Recall Memory
4. Forget Memory
5. View Important Memories
6. Memory Statistics
7. Auto Cleanup
8. Exit
```

---

## Example

Add Memory

```
Memory

User prefers Python for backend development.
```

Priority

```
High
```

---

Recall

Search

```
Python
```

Output

```
Memory Found

User prefers Python for backend development.

Priority

High

Recall Count

1
```

---

Memory Statistics

```
Total Memories : 12

High Priority : 4

Medium Priority : 5

Low Priority : 3

Total Recalls : 21
```

---

Auto Cleanup

```
Removed 3 unused low priority memories.
```

---

## Generated File

memory_store.json

Example

```json
[
    {
        "id": 1,
        "text": "User prefers Python for backend development.",
        "priority": "High",
        "created": "07-07-2026 18:20:45",
        "recall_count": 5
    },
    {
        "id": 2,
        "text": "User likes dark mode.",
        "priority": "Medium",
        "created": "07-07-2026 18:23:01",
        "recall_count": 2
    }
]
```

---

## Applications

- AI Assistant Memory
- Chatbot Context Management
- Knowledge Storage
- Personal Assistant Simulation
- Learning AI Concepts
- Conversation History Management

---

## Future Improvements

- Memory Categories
- Semantic Search
- Memory Relationships
- Importance Score
- Memory Decay
- Conversation Sessions
- Pin Important Memories
- Import / Export Memory
- AI Summary Generation
- Duplicate Memory Detection
- Memory Timeline
- Memory Graph Visualization

---

## License

MIT License