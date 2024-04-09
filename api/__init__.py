from flask import Flask

app = Flask(__name__)

from api.lost_and_found_endpoints import *
from api.doctor_appointment_endpoints import *


