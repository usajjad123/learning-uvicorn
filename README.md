# learning-uvicorn

A hands-on exploration of Uvicorn and different ways to create ASGI applications in Python.

## Overview

This repository demonstrates various approaches to creating ASGI applications that can be served with Uvicorn:

1. **From Scratch**: A basic ASGI application implementation without any frameworks
2. **Using Starlette**: A lightweight ASGI framework/toolkit
3. **Using FastAPI**: A modern, fast web framework for building APIs

## Contents

- `main.py`: Contains implementations of ASGI applications using different approaches:
  - `app_from_scratch`: A basic ASGI application implementation
  - `app_from_starlette`: A Starlette-based application
  - `app_from_fastapi`: A FastAPI-based application

## Running the Examples

Each example can be run using Uvicorn. Here's how to run them:

```bash
# Run the from-scratch implementation
uvicorn main:app_from_scratch

# Run the Starlette implementation
uvicorn main:app_from_starlette

# Run the FastAPI implementation
uvicorn main:app_from_fastapi
```

## Requirements

- Python >=3.13,<4.0
- Uvicorn
- Starlette
- FastAPI

## Installation

###  Virtualenv to isolate installation

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Using pip

```bash
pip install uvicorn starlette fastapi
```


### Using Poetry

```bash
# Install Poetry if you haven't already
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install

# Activate the virtual environment
poetry shell
```

## Purpose

This repository serves as a learning resource to understand:
- How ASGI applications work at a fundamental level
- Different ways to create ASGI-compatible applications
- The relationship between Uvicorn and various web frameworks
- The trade-offs between different approaches

## License

MIT