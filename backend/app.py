from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route("/start-bot", methods=["POST"])
def start_bot():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    min_interval = data.get("min_interval")
    max_interval = data.get("max_interval")

    try:
        # Zugangsdaten speichern
        with open("credentials.txt", "w") as f:
            f.write(f"{username}\n{password}")

        # Starte das Bot-Skript im Hintergrund
        subprocess.Popen(["python", "travian_bot.py", str(min_interval), str(max_interval)])

        return jsonify({"message": "Bot started successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
