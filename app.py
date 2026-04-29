from flask import Flask

# 1. Initialize the app
app = Flask(__name__)

# 2. Define the 'front door' (route) 
@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/new")
def new():
    return "NEW WORLD!"


# 3. Start the server
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000)