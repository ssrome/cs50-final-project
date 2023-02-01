from flask import Flask, redirect, render_template
from datetime import date
# import os                                            

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

@app.route("/")
def index():
    eventLists = [{"id": 1, "name": "Easter Monday"}, {"id": 2, "name": "Eurovision"}, {"id": 3, "name": "Christmas"}]
    return render_template("index.html", eventLists=eventLists, test="Year goes here")

if __name__ == "__main__": 
   app.run(debug=False, host='0.0.0.0')
    # port = int(os.environ.get('PORT', 5000))
    # app.run(debug=True, host='0.0.0.0', port=port)