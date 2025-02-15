from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']
    return (
            f"For the given statement, the system response is "
            f"'anger': {anger_score:.9f}, 'disgust': {disgust_score:.9f}, 'fear': {fear_score:.9f}, "
            f"'joy': {joy_score:.9f} and 'sadness': {sadness_score:.9f}. "
            f"The dominant emotion is <strong>{dominant_emotion}.</strong>"
        )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)