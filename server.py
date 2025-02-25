"""
This module provides Flask routes for an Emotion Detector application.
The application is designed to be run on a Flask server.

"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the emotions of the provided text and return the results.

    This function retrieves text from the query parameter 'textToAnalyze', checks 
    if the text is valid, and passes it to the emotion detection function.
    It then formats and returns a response that includes emotion scores and 
    the dominant emotion.

    """

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Check if the text is blank or None
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    # Pass the text to the emotion detector function and store the response
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
    """
    This functions renders the webpage to display the input field, button, and response

    """

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
    