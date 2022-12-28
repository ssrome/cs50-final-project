# ToDo App

#### Video Demo: <URL HERE>

#### Description:

A Python app with Flask

### Run development server

```bash
FLASK_APP=src/app flask run
```

### Run tests

```bash
nose2 -v
```

### Update requirements file

```bash
pip freeze > requirements.txt
```

### Install packages listed on requirements file

```bash
pip install -r requirements.txt
```

### Test coverage

```bash
coverage run tests
```

### Test coverage report

```bash
coverage report src/*.py
```
