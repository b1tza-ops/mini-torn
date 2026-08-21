from flask import Flask, render_template, request, redirect, session

from database.setup import create_tables
from database.users import get_user_by_username
from database.players import get_player_by_user_id
from utils.security import verify_password
from game.player import Player


app = Flask(__name__)

app.secret_key = "dev-secret-change-later"

create_tables()


@app.route("/")
def home():
    if "user_id" not in session:
        return redirect("/login")

    player_data = get_player_by_user_id(session["user_id"])

    if player_data is None:
        return "No character found."

    player = Player(*player_data)

    return render_template(
        "dashboard.html",
        player=player
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = get_user_by_username(username)

        if user is None:
            error = "User not found."

        elif not verify_password(password, user[3]):
            error = "Incorrect password."

        else:
            session["user_id"] = user[0]
            return redirect("/")

    return render_template(
        "login.html",
        error=error
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)