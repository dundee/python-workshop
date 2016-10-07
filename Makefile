
run:
	python3.5 main.py

mypy:
	python3.5 -m mypy -s chat

tests:
	python3.5 -m pytest tests/test_*.py

.PHONY: run tests
