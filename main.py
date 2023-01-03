from flask import Flask, jsonify, request
from datadome import Datadome
import os


app = Flask(__name__)
app.debug = True


@app.route("/datadome", methods=["POST"])
def handle_datadome():
    params = request.args.to_dict()

    domain = params.get("domain") or "https://www.footlocker.com/"
    cookie = Datadome().generate(domain)

    if cookie is not None:
        return jsonify(cookie)
    else:
        return "", 400


if __name__ == "__main__":
    app.run(port=os.getenv("PORT", default=5000))