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
    return render_template("gad.html")

@app.route("/ai")
def ai():
    return render_template("ai.html")

@app.route("/smartphone")
def smartph():
    return render_template("smartph.html")

@app.route("/innovtion")
def innovation():
    return render_template("innovtion.html")

@app.route("/laptops")
def lapptops():
    return render_template("laptops.html")

@app.route("/smartwatch")
def smarywht():
    return render_template("smartwatch.html")

@app.route("/cybersecurity")
def cybersrc():
    return render_template("cybersecurity.html")



app.run(debug=True)