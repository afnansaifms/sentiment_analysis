from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
import os

# Get absolute path of project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)


# Sentiment Analysis Function
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, polarity


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# API route
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "Please enter some text"}), 400

    sentiment, polarity = analyze_sentiment(text)

    return jsonify({
        "sentiment": sentiment,
        "polarity": round(polarity, 2)
    })


if __name__ == "__main__":
    print("Template folder:", app.template_folder)
    print("Static folder:", app.static_folder)
    app.run(debug=True)