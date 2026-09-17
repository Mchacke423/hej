from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route("/")
def forside():
    return f"<h1>Hej Mathias</h1><p>I dag er det {date.today()}</p>"

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
