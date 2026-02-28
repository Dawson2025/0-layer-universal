# Stage Manager Hand Off Documents

Task handoffs for stage management operations.

## Structure

```
hand_off_documents/
├── README.md           # This file
├── incoming/           # Tasks to be processed
│   └── README.md
└── outgoing/           # Completed task reports
    └── README.md
```

## How It Works

1. **Incoming tasks** are placed in `incoming/` with a description of what needs to be done
2. **Stage Manager** processes the task
3. **Completion report** is placed in `outgoing/`

## Document Naming

```
incoming/
  YYYYMMDD_task_description.md

outgoing/
  YYYYMMDD_completed_description.md
```
