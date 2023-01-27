install:
	pip install -r requirements.txt

.PHONY: install

test:
	pytest

.PHONY: test

run-dev:
	FLASK_APP=app flask run --debugger

.PHONY: run-dev

update-req:
	pip freeze > requirements.txt

.PHONY: update-req