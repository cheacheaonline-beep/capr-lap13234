from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

ADMIN_EMAIL = "admin@site.com"
ADMIN_PASSWORD = "1234"

attempts = 0
success = 0
fail = 0
logs = []

@app.route("/")
def home():
    return send_from_directory("", "index.html")

@app.route("/login", methods=["POST"])
def login():
    global attempts, success, fail

    data = request.json
    email = data.get("email")
    password = data.get("password")

    attempts += 1
    logs.append(f"{email} | {password}")

    if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
        success += 1
        return jsonify({"status": "success", "message": "✔ Login OK"})
    else:
        fail += 1
        return jsonify({"status": "fail", "message": "❌ Wrong credentials"})

@app.route("/stats")
def stats():
    return jsonify({
        "attempts": attempts,
        "success": success,
        "fail": fail,
        "logs": logs[-10:]
    })

app.run(debug=True)