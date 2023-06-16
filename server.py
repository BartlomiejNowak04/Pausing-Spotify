from flask import Flask, request
from flask_cors import CORS, cross_origin
import main

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['POST'])
@cross_origin()
def result():
    print(request.form['foo'])
    if request.form['foo'] == 'true':
        main.pause()

    return 'Received !', 200
