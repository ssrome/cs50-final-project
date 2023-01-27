FROM python:3.8-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

# RUN FLASK_APP=app flask run --debugger

CMD ["python" , "app.py" ]