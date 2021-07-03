from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        headers = list(request.headers)
        headers.append(("Remote-Address", request.remote_addr))
        headers.append(("Request-Method", request.method))
        headers.sort()
        headers = dict(headers)
        return headers


if __name__ == "__main__":
    app.run(debug=True)
