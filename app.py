from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def web():
    result = []
    if request.method == "GET":
        return render_template("index.html")
    else:
        label = request.form.get("fname")
        r = requests.get(
            "https://www.familug.org/search/label/{}".format(label))
        tree = BeautifulSoup(markup=r.text)
        node = tree.find_all("h3", attrs={'class': 'post-title entry-title'})
        for info in node:
            result.append((info.text, info.a.get("href")))
        return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
