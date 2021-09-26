from flask import Flask

# Initializes flask app
app = Flask(__name__)


# Home page display
@app.route("/")
def welcome():
    return "Welcome to python WebService"


@app.route("/gbenga/")
def hello():
    return "Hello Gbenga"


if __name__ != "__main__":
    pass
else:
    app.run()