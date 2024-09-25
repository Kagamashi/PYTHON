# Flask
# Flask is a lightweight web framework for building simple web applications.
# It provides flexibility, allowing you to add components as needed.
from flask import Flask # type: ignore
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
