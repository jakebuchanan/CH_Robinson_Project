from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        country = request.form["nm"]
        return redirect(url_for("user", cntry=country))
    else:
        return render_template("index.html")

@app.route("/<cntry>")
def user(cntry):
    countries = ["CAN","USA","MEX","BLZ","GTM","SLV","HND","NIC","CRI","PAN"]
    if cntry in countries:
        visited = []
        if(cntry == "CAN"):
            visited = ["USA","CAN"]
        elif(cntry == "USA"):
            visited = ["USA"]
        elif(cntry == "MEX"):
            visited = ["USA","MEX"]
        elif(cntry == "BLZ"):
            visited = ["USA","MEX","BLZ"]
        elif(cntry == "GTM"):
            visited = ["USA","MEX","GTM"]
        elif(cntry == "SLV"):
            visited = ["USA","MEX","GTM","SLV"]
        elif(cntry == "HND"):
            visited = ["USA","MEX","GTM","HND"]
        elif(cntry == "NIC"):
            visited = ["USA","MEX","GTM","HND","NIC"]
        elif(cntry == "CRI"):
            visited = ["USA","MEX","GTM","HND","NIC","CRI"]
        else:
            visited = ["USA","MEX","GTM","HND","NIC","CRI","PAN"]
        return f"<p>{visited}</p>"
    else:
        error = "Not a valid country, please go back to homepage and enter a valid country"
        return f"<p>{error}</p>"

if __name__ == "__main__":
    app.run()
