import time
import datetime
from flask import Flask, render_template, request
import json
from localStoragePy import localStoragePy
import os
from src.check_created_event import CheckCreatedEvent
from src.date_and_time import DateAndTime
from src.events import Events
from src.create_item import CreateItem


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
    current_year = DateAndTime.get_current_year()
    return dict(year=f'2022 - {current_year}')


@app.route("/", methods=["GET", "POST"])
def index():
    stored_item_list = "stored_item_list"
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
        previous_events = json.loads(localStorage.getItem(stored_item_list)) or []
        if checked_event is True:
            new_event = CreateItem(item_name).create_new_item()

            if previous_events is None or previous_events == []:
                localStorage.setItem(stored_item_list, json.dumps([new_event]))
                item_list = json.loads(localStorage.getItem(stored_item_list))

                return render_template("index.html", item_list=item_list)
            else:
                previous_events.extend([new_event])
                localStorage.setItem(stored_item_list, json.dumps(previous_events))
                return render_template("index.html", item_list=previous_events)
        return render_template("index.html", item_list=previous_events, error=True)

    elif method == "POST" and button_event in form:
        events = Events()
        item_list = json.loads(localStorage.getItem(stored_item_list))

        if button_event == "delete-all-event":
            updated_item_list = events(item_list, method, form)
        else:
            event_index = int(form.get(button_event))
            updated_item_list = events(item_list, method, form, event_index)

        localStorage.setItem(stored_item_list, json.dumps(updated_item_list))
        return render_template("index.html", item_list=updated_item_list)
    else:
        item_list = localStorage.getItem(stored_item_list)
        if item_list is None:
            localStorage.setItem(stored_item_list, '[]')
            return render_template("index.html")
        else:
            item_list = json.loads(localStorage.getItem(stored_item_list))
            return render_template("index.html", item_list=item_list)


@app.route("/completed")
def completed():
    stored_item_list = "stored_item_list"
    items = json.loads(localStorage.getItem(stored_item_list))
    filtered_completed_items = []

    for item in items:
        if item["is_complete"] is True:
            filtered_completed_items.append(item)

    return render_template("completed.html", item_list=filtered_completed_items)


@app.route("/add-countdown", methods=["GET", "POST"])
def add_countdown():
    stored_countdown_list = "stored_countdown_list"
    user_local_time = time.localtime()
    now = user_local_time
    form = request.form
    method = request.method
    button_event_list = list(form.to_dict().keys())

    if len(button_event_list) == 2:
        button_event = button_event_list.pop()
    elif len(button_event_list) == 1:
        button_event = button_event_list[0]
    else:
        button_event = None

    # ImmutableMultiDict([('new-countdown', 'test'),
    # ('countdown-date', '2023-03-07'),
    # ('countdown-time', '19:30'),
    # ('add-countdown-event', '')])

    countdown_date = form.get('countdown-date')
    countdown_time = form.get('countdown-time')
    user_timezone_str = time.strftime("%z", user_local_time)
    # time.strftime("%Y-%m-%d %H:%M:%S", user_local_time
    user_timezone = time.strptime(user_timezone_str, "%z")

    countdown_timestamp = f'{countdown_date} {countdown_time}{user_timezone}'
    # 2023-03-10 18:01+0000

    if request.method == "POST" and "add-countdown-event" in form:

        item_name = form.get("new-countdown")
        checked_event = CheckCreatedEvent.check_created_event(item_name)
        previous_events = json.loads(localStorage.getItem(stored_countdown_list)) or []
        if checked_event is True:
            new_event = CreateItem(item_name).create_new_countdown_item("2023-03-07 19:30+00:00")

            if previous_events is None or previous_events == []:
                localStorage.setItem(stored_countdown_list, json.dumps([new_event]))
                item_list = json.loads(localStorage.getItem(stored_countdown_list))

                return render_template("add-countdown.html", item_list=item_list)
            else:
                previous_events.extend([new_event])
                localStorage.setItem(stored_countdown_list, json.dumps(previous_events))
                return render_template("add-countdown.html",
                                       item_list=previous_events,
                                       countdown_timestamp=countdown_timestamp)

    elif method == "POST" and button_event in form:

        events = Events()
        item_list = json.loads(localStorage.getItem(stored_countdown_list))

        if button_event == "delete-all-event":
            updated_item_list = events(item_list, method, form)
        else:
            event_index = int(form.get(button_event))
            updated_item_list = events(item_list, method, form, event_index)

        localStorage.setItem(stored_countdown_list, json.dumps(updated_item_list))
        return render_template("add-countdown.html", item_list=updated_item_list,
                               error=True,
                               now=now,
                               countdown_timestamp=countdown_timestamp)

    else:
        item_list = localStorage.getItem(stored_countdown_list)
        if item_list is None:
            localStorage.setItem(stored_countdown_list, '[]')
            return render_template("add-countdown.html", now=now)
        else:
            item_list = json.loads(localStorage.getItem(stored_countdown_list))
            return render_template("add-countdown.html", item_list=item_list, now=now)


@app.route("/error")
def error():
    return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
