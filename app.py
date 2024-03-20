from flask import Flask, render_template, redirect, jsonify, request
from processor import SpiderModel, CustomModel

spidermodel = SpiderModel()
custommodel = CustomModel()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods = ["POST","GET"])
def final():
    if request.method == "POST":
        text = request.form["res"]
        model = request.form["mod"]

        print(model)

        if model == "Spider_T5":
            prediction = spidermodel.process(text)
        else:
            prediction = custommodel.process(text)

        print(prediction)

        return jsonify(prediction)


if __name__ == "__main__":
    app.run(debug=True)