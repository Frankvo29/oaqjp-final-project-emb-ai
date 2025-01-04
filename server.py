'''
This module provides a Flask-based web application for detecting emotions
in a given text input. It uses an external emotion detection library
(EmotionDetection.emotion_detection) to analyze the emotions present
in the text.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''
    This endpoint receives a text input via query parameters, passes it to the
    emotion detection library, and returns a formatted response with emotion scores
    and the dominant emotion.
    
    Returns:
        A string containing emotion scores (anger, disgust, fear, joy, sadness)
        and the dominant emotion if the text is valid.
        Otherwise, returns an error message.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    status_code = response.get("status_code")
    dominant_emotion = response.get("dominant_emotion")

    if status_code == 400 or dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger_score = response["scores"]["anger"]
    disgust_score = response["scores"]["disgust"]
    joy_score = response["scores"]["joy"]
    sadness_score = response["scores"]["sadness"]
    fear_score = response["scores"]["fear"]

    return (f"For the given statement, the system response is 'anger': {anger_score}, "
            f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score}, "
            f"'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}")

@app.route("/")
def render_index_page():
    '''
    Render the index page.
    This endpoint serves the main HTML page of the application.
    Returns:
        HTML: The rendered index.html page.
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
