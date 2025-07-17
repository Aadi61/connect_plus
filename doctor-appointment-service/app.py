from flask import Flask
from flask_cors import CORS
from routes import appointment_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(appointment_bp)

if __name__ == "__main__":
    app.run(port=5000,host="0.0.0.0", debug=True)
