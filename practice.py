from flask import Flask, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

# This route is a good example
@app.route('/user/<name>')
def hello_user(name):
   return '<h1>Hello {0}</h1>'.format(name)

@app.route('/form',methods= ['POST','GET'])
def enter_data():
    s = """<!DOCTYPE html>
<html>
<body>

<form action="http://localhost:5000/result" method="GET">
  URL:<br>
  <input type="text" name="url" value="http://nytimes.com">
  <br>
  <input type="submit" value="Submit">
</form> 

</body>
</html>""" 
# Note that by default http://nytimes.com would be entered in the input field
    return s

@app.route('/result',methods = ['POST', 'GET'])
def res():
    if request.method == 'GET':
        result = request.args
        url = result.get('url')
        print(url) 
        # What do you expect the print statement to print? 
        # Check the terminal to see what is printed
        # return requests.get(url).text
        ## Modify the function code and return statement 
        ## to display raw HTML data from http://nytimes.com
        soup = BeautifulSoup(urlopen(url).read(), "html.parser")
        print(soup.h2)
        return "test"
if __name__ == '__main__':
    app.run()