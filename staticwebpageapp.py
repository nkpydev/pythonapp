from flask import Flask, render_template

app = Flask(__name__)

app.config["SECRET_KEY"] = "ad85669cb9a22692a23d23a6c983f009"


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)