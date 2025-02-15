from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__) 

@app.route("/emotionDetector", methods=['GET'])
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Error: Please provide text to analyze using the 'textToAnalyze' query parameter.", 400

    response = emotion_detector(text_to_analyze)

    try:  # Handle potential KeyError if 'dominant_emotion' or score is missing
        dominant_emotion = response['dominant_emotion']
        dominant_emotion_score = response['scores'][dominant_emotion] # Correct way to access the score

    except KeyError as e:
        return f"Error processing emotion analysis: {e}.  Check the structure of the emotion_detector response.", 500  # More informative error


    return f"For the given statement, the dominant emotion is '{dominant_emotion}' with a score of {dominant_emotion_score:.2f}."

@app.route("\")
def render_index_page():
    return render_template('index.html') 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)  # debug=True for easier development