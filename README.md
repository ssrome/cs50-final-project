# ToDo App

#### Video Demo: <URL HERE>

#### Description:

A Python app with Flask

### Install packages listed on requirements file

```bash
pip install -r requirements.txt
```

If using pip3:

```
pip3 install -r requirements.txt
```

### Activate environment

```
source [name]/bin/activate
```

### Run inside environment

```
FLASK_APP=app flask --debug run
```

### Run development server outside environment

```bash
make run-dev
```

### Run production
```bash
make run-prod
```

## Testing

### Run tests

```bash
make test
```

### Test coverage

```bash
coverage run tests
```

### Test coverage report

```bash
coverage report src/*.py
```

### To run a report and watch tests

```bash
make watch-test-report
```

## Update requirements file

```bash
pip freeze > requirements.txt
```

If using pip3:

```
pip3 freeze > requirements.txt
```

## Docker

## Build

```
docker-compose up --build todo-dev
```

### Run in the backgroud

```
docker-compose up -d
```

### Stop it running

```
docker-compose stop
```
