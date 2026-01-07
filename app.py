from flask import Flask, render_template, request, redirect, session, jsonify
import requests

app = Flask(__name__)
app.secret_key = "chave-secreta"

API_KEY = "SUA_API_OPENWEATHER"
CIDADE = "Vitoria,BR"

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/auth", methods=["POST"])
def auth():
    usuario = request.form["usuario"]
    senha = request.form["senha"]

    if usuario == "admin" and senha == "123":
        session["logado"] = True
        return redirect("/dashboard")

    return redirect("/")

@app.route("/dashboard")
def dashboard():
    if not session.get("logado"):
        return redirect("/")
    return render_template("dashboard.html")

@app.route("/clima")
def clima():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"
    dados = requests.get(url).json()

    return jsonify({
        "temp": round(dados["main"]["temp"]),
        "desc": dados["weather"][0]["description"]
    })

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
