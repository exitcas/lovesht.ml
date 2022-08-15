import os, requests
from flask import Flask, make_response, redirect
app = Flask("44html's wildcard system")
app.config["SERVER_NAME"] = "lovesht.ml"
home = "https://44html.sape.gq/"

@app.route("/<root>")
def root(root): return redirect(f"{home}{root}")
@app.route("/<root>", subdomain="www")
def rootwww(): return root(root)
@app.route("/")
def main(): return redirect(home)
@app.route("/", subdomain="www")
def mainwww(): return home()


@app.route("/<filename>", subdomain="<user>")
def rooms(user, filename):
  c = requests.post(f"{home}~{user}/{filename}", data={"key": os.getenv("KEY")})
  r = make_response(c.text, c.status_code)
  r.headers["content-type"] = c.headers["content-type"]
  return r

@app.route("/", subdomain="<user>")
def roomhome(user):
  c = requests.post(f"{home}~{user}/", data={"key": os.getenv("KEY")})
  r = make_response(c.text, c.status_code)
  r.headers["content-type"] = c.headers["content-type"]
  return r
