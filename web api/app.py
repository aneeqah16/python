# This whole program is the server program using Flask

from flask import Flask, request  # Import Flask and request from flask

app = Flask(__name__)  # Create an instance of the Flask class

@app.route("/")  # Home route
# This function will be called when the home route is accessed
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/helloworld1")  # Route for /helloworld1
def hello_world1():
    return "<h1>Hello, World1</h1>"

@app.route("/helloworld2")  # Route for /helloworld2
def hello_world2():
    return "<h1>Hello, World2</h1>"

@app.route("/test")  # Route for /test
def test():
    a = 5 + 6  # Perform a simple addition
    return f"This is my function to run the app: {a}"  # Return the result

@app.route("/test2")  # Route for /test2
def test2():
    data = request.args.get('x')  # Get the 'x' parameter from the URL
    return f"This is a data input from my URL: {data}"  # Return the data

if __name__ == "__main__":
    app.run(host="0.0.0.0")  # Run the app on all available IP addresses