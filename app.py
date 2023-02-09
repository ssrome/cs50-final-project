from flask import Flask, render_template, request
from datetime import date
import uuid
import json
from localStoragePy import localStoragePy
import os

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
    year_now = today.strftime("%Y")
    return dict(year="2022 - {}".format(year_now))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST" and "submit-event" in request.form:
        previous_events = json.loads(localStorage.getItem("list")) or []
        
        event_id = uuid.uuid4().int
        new_event = {"id": event_id, "name": request.form.get("new-event")}
        if previous_events is None or previous_events == []:
            localStorage.setItem("list", json.dumps([new_event]))
            events = json.loads(localStorage.getItem("list"))
            return render_template("index.html", eventLists=events)
        else:
            previous_events.extend([new_event])
            localStorage.setItem("list", json.dumps(previous_events))
            return render_template("index.html", eventLists=previous_events)
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
    app.run(debug=True, port=os.getenv("PORT", default=5000))
