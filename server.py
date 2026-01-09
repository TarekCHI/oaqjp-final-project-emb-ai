"""
Flask server for Emotion Detection application.

Provides endpoints to:
- Render the home page (index.html)
- Detect emotions from user input via /emotionDetector
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_api():
    """
    Detect emotions from user-provided text.

    GET Parameters:
        textToAnalyze (str): The text input from the user.

    Returns:
        JSON response with formatted emotions or an error message
        if input is invalid or dominant emotion is None.
    """
    # Read query parameter sent by mywebscript.js
    text_to_analyse = request.args.get('textToAnalyze')

    # Handle blank or missing input
    if text_to_analyse is None or text_to_analyse.strip() == "":
        response = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        # Call emotion detector for valid input
        response = emotion_detector(text_to_analyse)

    # Check if dominant emotion is None
    if response['dominant_emotion'] is None:
        # Return a friendly error message
        return jsonify("Invalid text! Please try again!")

    # Extract emotion values
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Format output as requested
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return jsonify(formatted_response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    