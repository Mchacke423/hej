from flask import Flask
from datetime import date
import os

app = Flask(__name__)

@app.route("/")
def forside():
    return f"<h1>Se lige hvor dygtig Mathias Hacke er :)</h1><p>I dag er det {date.today()}</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
