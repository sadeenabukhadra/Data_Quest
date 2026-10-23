# Data Quest – Mastering Python Collections

## Description

Data Quest is a Python project focused on mastering built-in data structures and efficient data processing techniques through game-inspired scenarios.

The project explores how Python collections can be used to organize, manipulate, analyze, and process data. It covers practical programming concepts, from handling command-line arguments and calculating statistics to managing inventories, tracking achievements, generating event streams, and transforming data with comprehensions.

## Learning Objectives

- Understand and apply Python lists, tuples, sets, and dictionaries.
- Process command-line arguments and validate user input.
- Perform statistical calculations and data analysis.
- Use sets to identify unique, common, and missing elements.
- Manage structured data using dictionaries.
- Implement generators to produce and consume data on demand.
- Apply list and dictionary comprehensions for filtering and transformation.
- Handle exceptions and invalid inputs gracefully.
- Write clean, readable, and type-annotated Python code.

## Exercises

| Exercise | Description | Main Concepts |
|---|---|---|
| Command Quest | Process and display command-line arguments. | Lists, `sys.argv` |
| Score Cruncher | Analyze player scores and calculate statistics. | Lists, exception handling |
| Position Tracker | Store 3D coordinates and calculate distances. | Tuples, mathematical operations |
| Achievement Hunter | Compare player achievements and identify unique elements. | Sets, union, intersection, difference |
| Inventory Master | Manage inventory quantities and analyze item distribution. | Dictionaries, aggregation |
| Stream Wizard | Generate and consume randomized game events. | Generators, `yield`, lazy evaluation |
| Data Alchemist | Transform player names and filter scores efficiently. | List and dictionary comprehensions |

## Technologies

- **Language:** Python 3.10+
- **Standard Library:** `sys`, `math`, `random`, `typing`
- **Code Quality:** Flake8
- **Type Checking:** Mypy

## Project Structure

```text
.
├── ex0/
│   └── ft_command_quest.py
├── ex1/
│   └── ft_score_analytics.py
├── ex2/
│   └── ft_coordinate_system.py
├── ex3/
│   └── ft_achievement_tracker.py
├── ex4/
│   └── ft_inventory_system.py
├── ex5/
│   └── ft_data_stream.py
└── ex6/
    └── ft_data_alchemist.py
```

## Getting Started

### Prerequisites

- Python 3.10 or later

Check your Python version:

```bash
python3 --version
```

### Running the Exercises

Navigate to the desired exercise directory and run its Python script.

For example:

```bash
cd ex0
python3 ft_command_quest.py hello world
```

Run the score analysis exercise with sample input:

```bash
cd ex1
python3 ft_score_analytics.py 1500 2300 1800 2100 1950
```

Each exercise demonstrates a different approach to working with Python collections and processing data.

## Key Takeaways

This project highlights the importance of choosing the right data structure for a task. It develops practical skills in data organization, collection operations, input validation, lazy evaluation, and efficient data transformation.

The exercises provide a foundation for writing more structured, maintainable, and efficient Python programs.

---

**Topics:** Python · Data Structures · Collections · Data Processing · Generators · Comprehensions · Problem Solving
