from flask import Flask, render_template, request, redirect, url_for

#create a flask object
app = Flask(__name__)

#the home page for the website
@app.route("/", methods=["POST", "GET"])
def home():
    #user entered in country data
    if request.method == "POST":
        country = request.form["nm"]
        return redirect(url_for("user", cntry=country))
    #refresh of page or first time on page
    else:
        return render_template("index.html")

#the page to deal with country requests
@app.route("/<cntry>")
def user(cntry):
    #the list of North American country codes
    countries = ["CAN","USA","MEX","BLZ","GTM","SLV","HND","NIC","CRI","PAN"]

    #checks if input is a valid North American country code
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

    #invalid country code inputted
    else:
        error = "Not a valid country, please go back to homepage and enter a valid country"
        return f"<p>{error}</p>"

if __name__ == "__main__":
    app.run()
