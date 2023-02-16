from flask import Flask, render_template, request
import json
from localStoragePy import localStoragePy
import os

from src.events import Events
from src.get_current_year import GetCurrentYear
from src.event_item import EventItem
from src.delete import Delete
from src.update_complete_status import UpdateCompleteStatus

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
def inject_copyright_year():
    current_year = GetCurrentYear().__call__()
    return dict(year=f'2022 - {current_year}')


@app.route("/", methods=["GET", "POST"])
def index():
    method = request.method
    form = request.form
    if request.method == "POST" and "add-event" in request.form:
        previous_events = json.loads(localStorage.getItem("list")) or []
        event_name = request.form.get("new-event")
        new_event = EventItem(event_name).create_new_event()

        if previous_events is None or previous_events == []:
            localStorage.setItem("list", json.dumps([new_event]))
            events = json.loads(localStorage.getItem("list"))

            return render_template("index.html", eventLists=events)
        else:
            previous_events.extend([new_event])
            localStorage.setItem("list", json.dumps(previous_events))
            return render_template("index.html", eventLists=previous_events)
    elif request.method == "POST" and "delete-all" in request.form:
        cleared_list = Delete.delete_all([json.loads(localStorage.getItem("list"))])
        localStorage.setItem("list", cleared_list)
        return render_template("index.html")
    elif request.method == "POST" and "delete-event" in request.form:
        events = json.loads(localStorage.getItem("list"))
        event_index = int(request.form.get("delete-event"))
        updated_events = Delete.delete_item(events, event_index)
        localStorage.setItem("list", json.dumps(updated_events))
        return render_template("index.html", eventLists=updated_events)
    elif request.method == "POST" and "complete-event" in request.form:
        events = json.loads(localStorage.getItem("list"))
        event_index = int(request.form.get("complete-event"))
        updated_events = Events(UpdateCompleteStatus())(events, event_index, method, form)
        localStorage.setItem("list", json.dumps(updated_events))
        return render_template("index.html", eventLists=updated_events)
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
