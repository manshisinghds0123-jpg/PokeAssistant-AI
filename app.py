from flask import Flask, request, jsonify
from flask_cors import CORS
import threading

from assistant import speak

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "PokeAssist AI API Running"
    })


@app.route("/command", methods=["POST"])
def command():

    try:
        data = request.get_json()

        user_command = data.get("command")

        if not user_command:
            return jsonify({
                "error": "No command provided"
            }), 400


        response = process_command(user_command)

        return jsonify({
            "command": user_command,
            "response": response
        })


    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500



def process_command(command):

    command = command.lower()


    if "hello" in command:
        reply = "Hello Mansi, I am ready."


    elif "open chrome" in command:
        reply = "Opening Chrome"
        import os
        os.startfile(
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        )


    elif "open youtube" in command:
        reply = "Opening YouTube"
        import webbrowser
        webbrowser.open(
            "https://youtube.com"
        )


    elif "open google" in command:
        reply = "Opening Google"
        import webbrowser
        webbrowser.open(
            "https://google.com"
        )


    elif "open gmail" in command:
        reply = "Opening Gmail"
        import webbrowser
        webbrowser.open(
            "https://mail.google.com"
        )


    elif "open chatgpt" in command:
        reply = "Opening ChatGPT"
        import webbrowser
        webbrowser.open(
            "https://chatgpt.com"
        )


    elif "open vs code" in command:
        reply = "Opening Visual Studio Code"
        import os
        os.system("code")


    else:
        reply = "Sorry, I don't know this command yet."


    speak(reply)

    return reply



if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )