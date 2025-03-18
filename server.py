"Module Description"

from flask import Flask, render_template, request
from .emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    "Home page render"
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_handler():
    "API handling"
    try:
        emotions = emotion_detector(request.args["textToAnalyze"])

        if emotions["dominant_emotion"] == "None":
            return "Invalid text! Please try again!"
        response = (f"For given statements, the system response is 'anger': {emotions['anger']}, ",
        f"'disgust': {emotions['disgust']}, ",
        f"'fear': {emotions['fear']}, 'joy': {emotions['joy']}, 'sadness': {emotions['sadness']}.",
        f" The dominant emotion is {emotions['dominant_emotion']}.")
        return response
    except RuntimeError as e:
        return {"error": e}, 500

if __name__ == "__main__":
    app.run(debug=True)
