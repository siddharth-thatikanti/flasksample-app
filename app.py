from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello from Flask!</h1>
    <p>Your simple Flask app is running in Docker.</p>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    # Listen on all interfaces so Docker can publish the port.
    app.run(host="0.0.0.0", port=5000)
