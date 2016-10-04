
run:
	python3.5 main.py

tests:
	python3.5 -m pytest tests/test_*.py

.PHONY: run tests
