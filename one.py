from flask import Flask, render_template
app = Flask("News of modern technology")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/gadgets")
def gadgets():
    return render_template("gadgets.html")

@app.route("/ai")
def ai():
    return render_template("ai.html")

app.run(debug=True)