import game
from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# hakee tipit tietokannasta
@app.route('/fetchfirst/<country>')
def fetchfirst(country):
    first_hint = game.get_first_tip(country)
    result = {"first_hint": first_hint}
    resultjson = json.dumps(result)
    return resultjson # tee tästä response

@app.route('/fetchsecond/<country>')
def fetchsecond(country):
    second_hint = game.get_second_tip(country)
    result = {"second_hint": second_hint}
    resultjson = json.dumps(result)
    return resultjson # tee tästä response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


# second_tip = game.get_second_tip(country)
