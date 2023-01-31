from flask import Flask, redirect, render_template
# import os                                            

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache", "no-store", "must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    eventLists = [{"id": 1, "name": "birthday"}, {"id": 2, "name": "cinema"}, {"id": 3, "name": "sleeping"}]
    return render_template("index.html", eventLists=eventLists)

if __name__ == "__main__": 
   app.run(debug=False, host='0.0.0.0')
    # port = int(os.environ.get('PORT', 5000))
    # app.run(debug=True, host='0.0.0.0', port=port)