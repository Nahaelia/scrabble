import os
from flask import Flask, render_template, request, make_response, Response, jsonify

### CONFIGS
print(os.getenv('DEBUG'))

app = Flask(__name__)

app.config['DEBUG'] = os.getenv('DEBUG')
