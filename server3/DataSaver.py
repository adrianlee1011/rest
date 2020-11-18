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
    file.write(text + '|' + international + '|' + gerke + '|' + morse + '\n')
    file.close
    # Initialise string variables to be returned
    text = ""
    international = ""
    gerke = ""
    morse = ""
    # Get all records from data.txt file
    with open("data.txt") as file:
      for line in file:
        parts = line.split('|')
        text += parts[0] + '<br/>'
        international += parts[1] + '<br/>'
        gerke += parts[2] + '<br/>'
        morse += parts[3][:-1] + '<br/>'
    return json.loads('{"text":"' + text + '", "international":"' + international + '", "gerke":"' + gerke + '", "morse":"' + morse + '"}')

# Setup the Api resource routing
api.add_resource(DataSaver, '/<text>/<international>/<gerke>/<morse>')

# Setup port 5002
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5002)