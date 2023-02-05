from flask import Flask, redirect, render_template, request
from datetime import date
import uuid
import json
from localStoragePy import localStoragePy
# import os

localStorage = localStoragePy("cs50-todo", "text")
                                          
app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache", "no-store", "must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.context_processor
def inject_year():
    today = date.today()
    yearNow = today.strftime("%Y")
    return dict(year="2022 - {}".format(yearNow))

@app.route("/", methods=["GET", "POST"])
def index():
    
    if request.method == "POST" and "submit-event" in request.form:
    #     localStorage.clear()
        previousEvents = json.loads(localStorage.getItem("list")) or []
        
        id = uuid.uuid4().int
        newEvent = {"id": id, "name": request.form.get("new-event")}
        if previousEvents is None or previousEvents == []:
            localStorage.setItem("list", json.dumps([newEvent]))
            events = json.loads(localStorage.getItem("list"))
            return render_template("index.html", eventLists=events)
        else:
            previousEvents.extend([newEvent])
            localStorage.setItem("list", json.dumps(previousEvents))
            events = json.loads(localStorage.getItem("list"))
            return render_template("index.html", eventLists=previousEvents)
    elif request.method == "POST" and "delete-all" in request.form:
        localStorage.clear()
        localStorage.setItem("list", '[]')
        return render_template("index.html")
    else:
        events = localStorage.getItem("list")
        if events is None:
            localStorage.setItem("list", '[]')
            return render_template("index.html")
        else:
            events = json.loads(localStorage.getItem("list"))
            return render_template("index.html", eventLists=events)

@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == "__main__": 
    app.run(debug=False, host='0.0.0.0')
    # port = int(os.environ.get('PORT', 5000))
    # app.run(debug=True, host='0.0.0.0', port=port)