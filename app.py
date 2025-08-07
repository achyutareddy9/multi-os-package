from os import path, listdir
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Multi-OS Package!"})
@app.route('/files')
def list_files():
    files = [f for f in listdir('.') if path.isfile(f)]
    return jsonify({"files": files})
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
