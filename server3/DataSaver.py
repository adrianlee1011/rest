from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

import json

app = Flask(__name__)
api = Api(app)

# Store a new record and return all records
class DataSaver(Resource):
  def get(self, text, international, gerke, morse):
    # Write a new record into data.txt file
    file = open("data.txt", 'a')
    file.write(text + '$' + international + '$' + gerke + '$' + morse + '\n')
    file.close
    # Initialise string variables to be returned
    textArray = []
    internationalArray = []
    gerkeArray = []
    morseArray = []
    # Get all records from data.txt file
    with open("data.txt") as file:
      for line in file:
        parts = line.split('$')
        textArray.append(parts[0])
        internationalArray.append(parts[1])
        gerkeArray.append(parts[2])
        morseArray.append(parts[3][:-1])
        print(textArray)
    return json.loads('{"text":' + json.dumps(textArray) + ', "international":' + json.dumps(internationalArray) + ', "gerke":' + json.dumps(gerkeArray) + ', "morse":' + json.dumps(morseArray) + '}')

# Setup the Api resource routing
api.add_resource(DataSaver, '/<text>/<international>/<gerke>/<morse>')

# Setup port 5002
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5002)