from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

## Challenge 1
# If you go to http://localhost:5000/square, it would a display a form
# Update the view function that receives the data from the form and returns square of the number
@app.route('/square')
def squareView():
    html_form = '''
    <html>
    <body>
    <form method="GET" action="http://localhost:5000/result">
        <label>Enter the number you want to square:
            <input name="num" value="0" type="number">
        </label></br>
        <input type="submit" value="Submit">
    </form>
    </body>
    </html>
    '''
    return html_form

@app.route('/result', methods = ['GET', 'POST'])
def result_square():
    # Complete the function to return the appropriate data for the form above
    if request.method == "GET":
        return str(int(request.args["num"]) ** 2)


## Challenge 2
# Complete the function to return the appropriate data for the form below
# You have to return cube.html template, instead of returning a string.
# Think of what parameter should  be provided to render_template function
@app.route('/cube')
def cubeView():
    html_form = '''
    <html>
    <body>
    <form method="GET" action="http://localhost:5000/result-cube">
        <label>Enter the number you want to cube:
            <input name="num" value="0" type="number">
        </label></br>
        <input type="submit" value="Submit">
    </form>
    </body>
    </html>
    '''
    return html_form

@app.route('/result-cube', methods = ['GET', 'POST'])
def result_cube():
    if request.method == "GET":
        return render_template('cube.html', result = int(request.args["num"]) ** 3)



## Challenge 3
# This time we would return product.html as the template.
# However, product.html expects three variables
# How would you pass the parameters in render_template function to populate the placeholders in the template?
@app.route('/product')
def product():
    html_form = '''
    <html>
    <body>
    <form method="GET" action="http://localhost:5000/result-product">
        <label>Enter the number 1:
            <input name="num1" value="0" type="number">
        </label></br>
        <label>Enter the number 2:
            <input name="num2" value="0" type="number">
        </label></br>
        <input type="submit" value="Submit">
    </form>
    </body>
    </html>
    '''
    return html_form

@app.route('/result-product', methods = ['GET', 'POST'])
def result_product():
    if request.method == "GET": 
        num_1 = int(request.args["num1"])
        num_2 = int(request.args["num2"])
        print(num_1, num_2)
        return render_template('product.html', num1 = str(num_1), num2 = str(num_2), product = str(num_1 * num_2))


## Challenge 4
# Part 1: The form on http://localhost:5000/itunes-form allows user to enter artist name and select the number of results he/she wants from the API
# You have to first write the view to display the form on the screen. The form can be displayed by rendering itunes-form.html template.

# YOUR CODE FOR THE VIEW HERE
# What should be the value of the action attribute in the form i.e. itunes-form.html?
# What should be the value of the method attribute in the form i.e. itunes-form.html?
@app.route('/itunes-form')
def itunes_form():
    return render_template('itunes-form.html')

# Part 2: Next, you have to use the template "list.html" to display the results for the choices entered by the user in the form above.
# The data should be displayed on http://localhost:5000/itunes-result
# YOUR CODE FOR THE VIEW HERE
@app.route('/itunes-result')
def itunes_result():
    options = {}
    options['term'] = request.args['artist']
    options['limit'] = request.args['num']
    result = json.loads(requests.get('https://itunes.apple.com/search', params = options).text)['results']
    return render_template('list.html', results = result)
# Specify the route and write the cooresponding view function
# How would you extract the data the you have received from the form, and prepare the API request URL?


## BONUS CHALLENGE
# Can you think of replacing the redunant html strings in challenges 1 and 2?
# Can we write a single template for both /square and /cube views?
#### allow user to choose square or cube

if __name__ == '__main__':
    app.run(debug=True)
