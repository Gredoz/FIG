from flask import Flask, render_template, request
import util
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        query = request.form.get("query")
        results = util.find(query)
        if results is None:
            return render_template("index.html",query=query,error="Your query is not valid")
        return render_template("index.html",query=query,results=results)
        
if __name__ == "__main__":
    app.debug = True;
    app.run("0.0.0.0",8000)
