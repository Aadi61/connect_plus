from flask import Flask
from flask_cors import CORS
from routes import carpool_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(carpool_bp)

print("Registered routes:")
for rule in app.url_map.iter_rules():
    print(rule)

if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")
