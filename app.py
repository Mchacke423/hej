from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route("/")
def forside():
    return f"<h1>Hej Mathias</h1><p>I dag er det {date.today()}</p>"

if __name__ == "__main__":
    app.run(debug=True)
