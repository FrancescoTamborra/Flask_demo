from flask import Flask, render_template

#print(__name__)
app = Flask(__name__) # we run it as main, see below

# But first we need to define a route otherwise, even if the app is running on localhost we get a 404

@app.route('/') # we use a decorator for the next function applied to the route /
@app.route('/index') # we can apply the same function index to multiple routes
def index():
    return render_template('index.html', current_title='Custom Title') # Flask has Jinja tamplate engine which allows to render much more than plain html (dynamic)

if __name__ == '__main__':
    app.run(debug=True) # always use degug in order to have useful info from Flask
    # notice that when you save the app is updated and restarted; don't need to ctrl+c and run it again
