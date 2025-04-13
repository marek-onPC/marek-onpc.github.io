.PHONY: test

format:
	isort . && black . && flake8 . && mypy .

test:
	poetry run python -m pytest . -vv

start:
	poetry run uvicorn main:app --host 0.0.0.0 --port 8000

