from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        query = request.form.get("query")
        return render_template("index.html")
        
if __name__ == "__main__":
    app.debug = True;
    app.run("0.0.0.0",8000)
