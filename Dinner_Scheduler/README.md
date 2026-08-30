# Dinner Scheduler

A simple Python command-line program that randomly selects a dinner dish without repeating dishes until the available list has been exhausted.

## How It Works

1. The program checks whether the dinner schedule file exists.
2. It reads the available dishes.
3. A random dish is selected.
4. The selected dish is removed from the available list.
5. The selected dish is saved to a separate file.
6. When all dishes have been used, the used dishes are returned to the available list.
7. The process starts again.

## Requirements

- Python 3

## Run

```bash
python3 dinner_scheduler.py
