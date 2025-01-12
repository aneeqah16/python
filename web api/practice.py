from flask import Flask, request  # Import Flask and request from flask
app = Flask(__name__)  # Create an instance of the Flask class
app.route("/")
def greeting_page():
    return "<h1>Welcome to the greeting page</h1>"

@app.route("/greet")
def greet():
    name = request.args.get('name')
    return f"<h1>Hello, {name}!</h1>"

@app.route("/products")
def products():
    return "<h1>Products</h1>"
@app.route("/feedback")
def feedback():
   feed = request.args.get('feedback')
   return f"<h1>Feedback: {feed}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")  # Run the application on host


