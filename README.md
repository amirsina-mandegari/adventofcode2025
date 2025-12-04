# Advent of Code 2025 Solutions

Welcome to my Advent of Code 2025 repository! This repo contains my solutions to the Advent of Code 2025 challenges, solved using Python. Each day has its own folder with the corresponding solution for that day's puzzle.

## Table of Contents

- [About Advent of Code](#about-advent-of-code)
- [Repository Structure](#repository-structure)
- [Usage](#usage)
- [Languages](#languages)
- [Contributing](#contributing)
- [License](#license)

## About Advent of Code

[Advent of Code](https://adventofcode.com/) is an annual event in December, where a new coding puzzle is released each day. Each puzzle requires creative problem-solving and coding skills. The puzzles range in difficulty, and solutions are often written in a variety of programming languages.

The event begins on December 1st, with a new challenge each day leading up to Christmas Eve. It's a fun way to learn, practice programming, and get into the holiday spirit!

## Repository Structure

The structure of this repository is organized by day. Each day's challenge is contained within its own folder, and the solution for that day is inside a Python file named `solution.py`.

```
adventofcode2025/
├── day01/
│   ├── solution.py
│   └── input
├── day02/
│   ├── solution.py
│   └── input
├── day03/
│   ├── solution.py
│   └── input
...
```

Each folder is named by the day of the challenge (e.g., `day01`, `day02`, etc.), and each contains a Python file `solution.py` with the code that solves the problem for that day, along with an `input` file containing the puzzle input.

## Usage

To view and run the solutions locally, clone this repository to your machine:

```bash
git clone https://github.com/yourusername/adventofcode2025.git
cd adventofcode2025
```

### Setup

This project uses [UV](https://github.com/astral-sh/uv) for fast Python package management and [pre-commit](https://pre-commit.com/) for code quality checks.

#### Installing UV

Install UV using one of the following methods:

**macOS/Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Or using pip:

```bash
pip install uv
```

#### Installing Dependencies

After installing UV, install the project dependencies (including pre-commit):

```bash
uv pip install pre-commit
```

The dependencies are listed in `pyproject.toml` for reference, but since this is a script-based project (not an installable package), you can install dependencies directly with UV.

#### Initial Setup

1. Install pre-commit hooks:

```bash
pre-commit install
```

2. (Optional) Run pre-commit on all files:

```bash
pre-commit run --all-files
```

### Running Solutions

Each day's solution is in a separate folder. You can navigate to the corresponding day's folder and run the solution. For example, for Day 1:

```bash
cd day01
python solution.py
```

The solutions are written in Python, so you will need Python 3.x installed on your machine. You can download Python from [here](https://www.python.org/downloads/).

### Pre-commit Hooks

This repository uses pre-commit hooks to ensure code quality. The hooks will automatically run on each commit and check for:

- Trailing whitespace
- End of file formatting
- YAML/JSON/TOML syntax
- Code formatting (Black and Ruff)
- Debug statements
- Merge conflicts

You can manually run the hooks at any time:

```bash
pre-commit run --all-files
```

## Languages

All solutions in this repository are written in **Python**. If you want to use another language or modify the code for optimization, feel free to do so!

## Contributing

While this repository is intended to document my own solutions, feel free to fork it, suggest improvements, or share your own solutions to the Advent of Code challenges! If you want to contribute or have any suggestions, please feel free to open an issue or pull request.

If you'd like to contribute, please ensure that your code follows the same structure and style as the existing solutions.

## License

This repository is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy coding and enjoy the challenge! 🎄
