install:
	pip install -r requirements.txt

.PHONY: install

test:
	pytest

.PHONY: test

run-dev:
	FLASK_APP=app flask --debug run

.PHONY: run-dev

update-req:
	pip freeze > requirements.txt

.PHONY: update-req

watch-test-report:
	pytest-watch --beforerun "pytest --html=./test-report.html --self-contained-html"
.PHONY: watch-test-report

watch-test:
	pytest-watch
.PHONY: watch-test

run-prod:
    gunicorn app:app
.PHONY: run-prod