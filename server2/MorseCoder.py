from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

import json

app = Flask(__name__)
api = Api(app)

# Modern International Morse code character dictionary
international_dict = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-', '&':'·-···', ':':'---···', ';':'-·-·-·', '=':'-···-', '+':'·-·-·', '-':'-····-', '_':'··--·-', '\"':'·-··-·', '$':'···-··-', '@':'·--·-·', ' ':'/'}

# Continental Gerke code character dictionary
gerke_dict = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'..', 'k':'-.-', 'l':'-', 'm':'--', 'n':'-.', 'o':'..', 'p':'....', 'q':'..-.', 'r':'...', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'.-..', 'y':'....', 'z':'....', '1':'.--.', '2':'..--..', '3':'...-.', '4':'....-', '5':'---', '6':'......', '7':'--..', '8':'-....', '9':'-..-', '0':'-----', ' ':'/'}

# American (original) Morse code character dictionary
morse_dict = {'a':'.-', 'b':'-...', 'c':'...', 'd':'-..', 'e':'.', 'f':'.-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'-.-.', 'k':'-.-', 'l':'-', 'm':'--', 'n':'-.', 'o':'.-...', 'p':'....', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'..-...', 'y':'--...', 'z':'.--..', '1':'.--.', '2':'..--..', '3':'...-.', '4':'....-', '5':'---', '6':'......', '7':'--..', '8':'-....', '9':'-..-', '0':'-----', ' ':'/'}

# Take text as an argument and returns Morse code translation,
# dict argument determines which dictionary is going to be used;
# '1' - international, '2' - Gerke, '3' - Morse.
def translate(text, dict):
  code = ""
  if dict == 1:
    dictionary = international_dict
  if dict == 2:
    dictionary = gerke_dict
  if dict == 3:
    dictionary = morse_dict
  for char in text.lower():
    try:
      code += dictionary[char] + ' '
    except:
      code += char + ' '
  return code

# Return three different Morse code translations to the call
class MorseCoder(Resource):
  def get(self, text):
    international = translate(text, 1)
    gerke = translate(text, 2)
    morse = translate(text, 3)
    return json.loads('{"international":"' + international + '", "gerke":"' + gerke + '", "morse":"' + morse + '"}')

# Return specified Morse code translation to the call
class MorseCoderSpecific(Resource):
  def get(self, text, dictionary):
    if dictionary == "international":
      dict = 1
    if dictionary == "gerke":
      dict = 2
    if dictionary == "morse":
      dict = 3
    code = translate(text, dict)
    return json.loads('{"' + dictionary + '":"' + code + '"}')

# Setup the Api resource routing
api.add_resource(MorseCoder, '/<text>')
api.add_resource(MorseCoderSpecific, '/<text>/<dictionary>')

# Setup port 5001
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5001)