# SI364 Section W3 | Jan 15-16 | Templates, More Practice 

# Link to this document : https://goo.gl/VVuuGD
# Lecture Links 
- +SI 364 | W18 | Lecture 1 | January 5, 2018 
- +SI 364 | W18 | Lecture 2 | January 12, 2018 
# Diagramming 
## Task 1 (10-15 minutes) 

Work with your groups on the white boards to diagram the flow of data for the Flask application shown below. Diagram for the instances

- When one types http://localhost:5000 in the browser
- When one types http://localhost:5000/music/titanic in the browser
- When one types http://localhost:5000/findcoolstuff/music/beatles
- When one types http://localhost:5000/findcoolstuff

Consider which view function is accessed in each instance, and what data is returned to the browser. 


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


# Templates 
- Templates have placeholders for dynamic content.


    <html>
      <body>
          <h1>Hello, {{ firstname }}!</h1>
      </body>
    </html>


- Templates can be rendered using render_template. One has to specify the following as parameters when using render_template:
  - template name as a string
  - variables that appear within the template and their corresponding values


    from flask import Flask, render_template
    app = Flask(__name__)
    app.debug = True
    
    @app.route('/') # http://localhost:5000/
    def hello_to_you():
        # return "Hello!"
        return render_template('hello.html', firstname='Jim!') # Rendering the template hello.html
    if __name__ == '__main__':
        app.run()


- We can make more complicated templates to deal with large chunks of data. One can write loops within templates to deal with a sequence of data. Example, if you had a list of names, and you wanted to display each name on a single line. 
- Let’s try to render this template


    <!-- Languages : ['Python', 'C++', 'C', 'Java', 'JavaScript']
    -->
    <html>
      <head>
        <title>Simple Flask App</title>
      </head>
      <body>
        {% for n in languages %}
        <h1>{{ n }}</h1>
        {% endfor %}
      </body>
    </html>
## Task 2: Practice with forms and templates (30 minutes)

Let’s apply what we have learned about templates just now. 

Download the files from Canvas > Files > Section_Week3 folder. There are HTML files in the template folder, and a challenges.py file which is a simple flask application. There are 4 challenges related to forms and templates in challenges.py. 


# Review of Python and Flask (15-20 minutes) 
- Functions besides view functions
- Other Python structures — like classes
- You can build “helper code” and use it inside view functions, invoke other functions inside view functions, imported or not (as long as it’s imported properly)
## Practice, # 1
    from flask import Flask, request
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
            return "Hello world!"
            ## Modify the function code and return statement 
            ## to display raw HTML data from http://nytimes.com
    
    if __name__ == '__main__':
        app.run()


- Copy-paste the code above to your text editor (Sublime or Atom etc) and try editing it so that you can build a flask application where you submit http://nytimes.com in the form
- Upon submission, data is fetched from http://nytimes.com and displayed on the screen
- **For reference:** ****Fetching data from a page on the internet https://www.programsinformationpeople.org/runestone/static/publicpy3/Requests/fetching_a_page.html


## Practice, # 2

If you are done with the task above, awesome! Let’s build on that…
Modify the code you have written so far:

- Use BeautifulSoup to find all the headlines from the New York Times. 
  - Right click on few articles and headlines and select “Inspect Element”. What do you think is the common attribute in the tags of these HTML elements? 
  - Reference : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Write code to display all the article headings on the screen. Think about how you can modify the function `res`, that receives data from the HTML form.


## Practice, # 3

Going further… 
Modify the code to display only the first 5 headlines, with each headline on a separate line. 

There are 2 ways to do this:

- **Either** : How can you “concatenate” the headlines and their URLs, and display each headline on one line. 
- **Or** : Use templates to loop through the headlines and display them 
![](https://www.dropbox.com/s/upqt176ui1u9kf2/Screenshot%202017-09-13%2000.57.21.png?raw=1)

## Practice, #4
- Now initialize a local git repository in the folder where you are working. 
- After initializing, stage the files for commit
- Next, commit the changes to the local repo
- Create a repository on github
- Finally, push the changes to the repository you created

HINT : Refer to this [Git Cheatsheet](https://scotch.io/bar-talk/git-cheat-sheet)

[](https://www.git-tower.com/blog/git-cheat-sheet/)

