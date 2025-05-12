from flask import Flask, request, jsonify

app = Flask(__name__)

latest_command = None
latest_status = None

@app.route('/command', methods=['POST'])
def set_command():
    global latest_command
    latest_command = request.json
    return jsonify({"success": True, "message": "Command received"})

@app.route('/get-command', methods=['GET'])
def get_command():
    return jsonify(latest_command or {})

@app.route('/status', methods=['POST'])
def set_status():
    global latest_status
    latest_status = request.json
    return jsonify({"success": True})

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(latest_status or {})

@app.route('/')
def home():
    return "ESP32 Server is running."
