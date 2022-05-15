.PHONY: test

test:
	PYTHONPATH=. pytest

test-print:
	PYTHONPATH=. pytest -s
