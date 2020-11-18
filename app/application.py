from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

app_id = 'fc0e4242'
app_key = 'fe1556577c601ca496e9a80c66041985'

@app.route("/", methods=["GET"])
def index():
    # quote = requests.get("http://127.0.0.1:5001/ahojadrian123456/international")
    # if not quote.ok:
    #     quote = None
    # quote = quote.json()

    # url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/en-gb/" + 'activity'.lower()
    # r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
    # r = r.json()

    return render_template("client.html")


@app.route("/coder", methods=['POST'])
def coder():
    # Query for text to translate to morse code
    text = request.form.get("text")
    res = requests.get("http://127.0.0.1:5001/" + text)
 
    # Make sure request succeeded
    if res.status_code != 200:
        return jsonify({"success": False})
 
    data = res.json()
    
    writeRes = requests.get(f"http://127.0.0.1:5002/{text}/{data['international']}/{data['gerke']}/{data['morse']}")

    return jsonify({"success": True, "code": data})


@app.route("/dictionary", methods=['POST'])
def dictionary():
    # Query for text to translate to morse code
    word = request.form.get("word")
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/en-gb/" + word.lower()
    res = requests.get(url, headers={'app_id' : app_id, 'app_key' : app_key})

    # Make sure request succeeded
    if res.status_code != 200:
        return jsonify({"success": False})
 
    data = res.json()
    return jsonify({"success": True, "word": data})

    