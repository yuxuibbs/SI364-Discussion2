from flask import Flask, render_template
app = Flask(__name__)
app.debug = True

@app.route('/') # http://localhost:5000/
def hello_to_you():
    # return "Hello!"
    return render_template('hello.html', firstname='Jim!') # Rendering the template hello.html
if __name__ == '__main__':
    app.run()