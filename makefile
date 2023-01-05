.PHONY: init lint test

init:
	virtualenv venv
	venv/bin/pip install -e '.[tests]'

lint:
	venv/bin/black .

test:
	venv/bin/python -m unittest tests
