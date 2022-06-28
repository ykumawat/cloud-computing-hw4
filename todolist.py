from flask import Flask, render_template, redirect, g, request, url_for, jsonify, json
import urllib
import requests
import os

app = Flask(__name__)
# make sure to replace localhost with the actual IP of the backend service after you deploy the backend service on Google Cloud
# for example, like this: TODO_API_URL = "http://123.456.789.123:5001"
TODO_API_URL = "http://localhost:5001"


@app.route("/")
def show_list():
    resp = requests.get(TODO_API_URL+"/api/items")
    resp = resp.json()
    return render_template('index.html', todolist=resp)


@app.route("/add", methods=['POST'])
def add_entry():
    requests.post(TODO_API_URL+"/api/items", json={
                  "what_to_do": request.form['what_to_do'], "due_date": request.form['due_date']})
    return redirect(url_for('show_list'))


@app.route("/delete/<item>")
def delete_entry(item):
    item = urllib.parse.quote(item)
    item = urllib.parse.quote(item)
    requests.delete(TODO_API_URL+"/api/items/"+item)
    return redirect(url_for('show_list'))

@app.route("/mark/<item>")
def mark_as_done(item):
    item = urllib.parse.quote(item)
    requests.put(TODO_API_URL+"/api/items/"+item)
    return redirect(url_for('show_list'))


if __name__ == "__main__":
    app.run("0.0.0.0")


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


if __name__ == "__main__":
    app.run("0.0.0.0")
