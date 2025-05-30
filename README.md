# Fibonacci Parallelized
Project focused on implementing and experimenting with different Fibonacci algorithms, including several parallelization strategies to improve performance and efficiency.

> **Note:** This project is not finished and is currently under active development.
## Getting started
First, set up your Python environment:

```bash
python -m venv .venv

# On Windows:
.venv\Scripts\activate
# On Unix or MacOS:
source .venv/bin/activate

python -m pip install -e .
```

For available options and help, use:

```bash
fib --help
```

## Installation

Create a virtual environment and then install fibonacci-number:

```bash
pip install fibonacci-number
```

## Running with Docker

To build the Docker image:

```bash
docker build -t fib_api:latest .
```

To run the project in a container:

```bash
docker run --name fib_container -it --entrypoint bash fib_api:latest
```

## Development

For development and testing, install additional dependencies:

```bash
pip install -e ".[dev]"
```

Run the test suite with:

```bash
pytest tests/
```