import requests
from flask import Flask, make_response
app = Flask("44html subdomain")
app.config["SERVER_NAME"] = "44ht.ml"


@app.route("/<path:filename>", subdomain="<user>")
def roomsd(user, filename):
  c = requests.get(f"https://web.sape.gq/~{user}/{filename}")
  r = make_response(c.text), c.status_code
  r.headers["content-type"] = c.headers["content-type"]
  return r

@app.route("/", subdomain="<user>")
def roomhomesd(user):
  c = requests.get(f"https://web.sape.gq/~{user}/")
  r = make_response(c.text), c.status_code
  r.headers["content-type"] = c.headers["content-type"]
  return r
