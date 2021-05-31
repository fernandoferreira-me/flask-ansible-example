from flask import Flask, jsonify
app = Flask("flask_ansible_example")

@app.route("/")
def hello():
    return 'hello'

@app.route("/health")
def health():
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
