"""
pen http://127.0.0.1:5001 in your browser.
"""

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
total_minutes = 0
# Total minutes accumulated, kept in memory while the server runs.

@app.route("/")
def home():
    return render_template("index.html", total=total_minutes)


@app.route("/add", methods=["POST"])
def add():
    global total_minutes
    data = request.get_json(silent=True) or {}
    minutes = data.get("minutes", 0)
    try:
        minutes = int(minutes)
    except (TypeError, ValueError):
        minutes = 0
    total_minutes += minutes
    return jsonify(total=total_minutes)


if __name__ == "__main__":
    app.run(debug=True, port=5001)