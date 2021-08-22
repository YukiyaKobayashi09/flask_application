from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Flask!!!"

@app.route('/foo')
def foo():
    return "Foo page accessed."

if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)