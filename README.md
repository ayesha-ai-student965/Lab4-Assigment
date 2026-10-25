Lab 4: Git and NumPy

Project Overview

This project demonstrates Git version control, Python virtual environments, Jupyter notebooks, and NumPy operations.

Project Structure

- "data/": Raw and processed data
- "notebooks/": Jupyter notebooks for the lab
- "src/": Python utility functions
- "tests/": Tests for the utility functions
- "docs/": Lab notes and documentation

Setup

Create a virtual environment:

python -m venv venv

Activate it in Windows PowerShell:

.\venv\Scripts\Activate.ps1

Install the dependencies:

python -m pip install -r requirements.txt

Run Tests

python -m pytest -v

NumPy Performance

The lab compares Python loops with NumPy vectorisation using timing and memory measurements.