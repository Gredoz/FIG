from flask import Flask, render_template, request
import util
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        query = request.form.get("query")
        results = util.get_pages(query)
    return render_template("index.html")
        
if __name__ == "__main__":
    app.debug = True;
    app.run("0.0.0.0",8000)
