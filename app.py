from flask import Flask, render_template, request
import json
from localStoragePy import localStoragePy
import os
from src.check_created_event import CheckCreatedEvent
from src.events import Events
from src.get_current_year import GetCurrentYear
from src.event_item import EventItem


localStorage = localStoragePy("cs50-todo", "json")
                                          
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
    button_event_list = list(form.to_dict().keys())

    if len(button_event_list) == 2:
        button_event = button_event_list.pop()
    elif len(button_event_list) == 1:
        button_event = button_event_list[0]
    else:
        button_event = None

    if method == "POST" and "add-event" in form:
        item_name = form.get("new-item")
        checked_event = CheckCreatedEvent.check_created_event(item_name)
        previous_events = json.loads(localStorage.getItem("list")) or []
        if checked_event is True:
            new_event = EventItem(item_name).create_new_event()

            if previous_events is None or previous_events == []:
                localStorage.setItem("list", json.dumps([new_event]))
                item_list = json.loads(localStorage.getItem("list"))

                return render_template("index.html", item_list=item_list)
            else:
                previous_events.extend([new_event])
                localStorage.setItem("list", json.dumps(previous_events))
                return render_template("index.html", item_list=previous_events)
        return render_template("index.html", item_list=previous_events, error=True)

    elif method == "POST" and button_event in form:
        events = Events()
        item_list = json.loads(localStorage.getItem("list"))

        if button_event == "delete-all-event":
            updated_item_list = events(item_list, method, form)
        else:
            event_index = int(form.get(button_event))
            updated_item_list = events(item_list, method, form, event_index)

        localStorage.setItem("list", json.dumps(updated_item_list))
        return render_template("index.html", item_list=updated_item_list)
    else:
        item_list = localStorage.getItem("list")
        if item_list is None:
            localStorage.setItem("list", '[]')
            return render_template("index.html")
        else:
            item_list = json.loads(localStorage.getItem("list"))
            return render_template("index.html", item_list=item_list)


@app.route("/completed")
def completed():
    items = json.loads(localStorage.getItem("list"))
    filtered_completed_items = []

    for item in items:
        if item["is_complete"] is True:
            filtered_completed_items.append(item)

    return render_template("completed.html", item_list=filtered_completed_items)


@app.route("/add-countdown")
def add_countdown():
    return render_template("add-countdown.html")


@app.route("/error")
def error():
    return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
