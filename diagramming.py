import requests
import json
from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route('/') # http://localhost:5000/
@app.route('/index') 
@app.route('/home')
def hello_to_you():
    return 'Hello!'

@app.route('/findcoolstuff/<media>/<term>')
def get_data(media,term):
        # I want to make a request to the itunes api
        # I want parameters: term and media to have specific values
        baseurl = "https://itunes.apple.com/search"
        params = {}
        params["term"] = term
        params["media"] = media
        resp = requests.get(baseurl,params=params) # this will hold a response object
        data_text = resp.text 
        python_obj = json.loads(data_text)
        typ_obj = type(python_obj)
        #print(str(typ_obj))
        res = python_obj["results"]
        print(res)
        return str(res)

if __name__ == '__main__':
    app.run()