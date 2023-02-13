from flask import jsonify, render_template, request

from .app import app

@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")


@app.route("/greet", methods=["POST"])
def greet():
    json = request.get_json()

    firstName = json.get("firstName", "").strip()
    lastName = json.get("lastName", "").strip()

    errors = {}

    if not firstName:
        errors["firstName"] = "Required"

    if not lastName:
        errors["lastName"] = "Required"

    if errors:
        return jsonify({"answer" : "ok", "message" : "hello '{firstName} {lastName}'"})    
