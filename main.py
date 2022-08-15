import requests
from flask import Flask, make_response
app = Flask("44html subdomain")
app.config["SERVER_NAME"] = "44ht.ml"


@app.route("/<path:filename>", subdomain="<user>")
def roomsd(user, filename):
  c = requests.get(f"https://44ht.ml/~{user}/{filename}")
  r = make_response(c.text), c.status_code
  r.headers["content-type"] = c.headers["content-type"]
  return r

@app.route("/", subdomain="<user>")
def roomhomesd(user):
  c = requests.get(f"https://44ht.ml/~{user}/")
  r = make_response(c.text), c.status_code
  r.headers["content-type"] = c.headers["content-type"]
  return r

app.run(host="0.0.0.0")