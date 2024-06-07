from flask import Flask, request, jsonify

app = Flask(__name__)

HWID_DATA = {}

@app.route('/api/reset_hwid', methods=['POST'])
def reset_hwid():
    data = request.json
    key = data.get('key')
    if key in HWID_DATA:
        HWID_DATA[key] = None  # Reset HWID
        return jsonify({"message": "HWID reset successful"}), 200
    return jsonify({"message": "Invalid key"}), 400

@app.route('/api/update_hwid', methods=['POST'])
def update_hwid():
    data = request.json
    key = data.get('key')
    hwid = data.get('hwid')
    HWID_DATA[key] = hwid
    return jsonify({"message": "HWID updated"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
