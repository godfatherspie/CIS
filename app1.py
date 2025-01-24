from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple dictionary to simulate a user database with multiple users
users = {
    "anshuman": "anshuman2004",
    "user2": "password2",
    "user3": "password3"
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Check if username and password match
        if username in users and users[username] == password:
            return render_template("login.html", success=True)
        else:
            return render_template("login.html", error=True)

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
