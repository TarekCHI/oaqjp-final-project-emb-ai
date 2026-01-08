import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    input_json = {"raw_document": {"text": text_to_analyse}}  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=input_json, headers=header)  # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text) # Parsing the JSON response from the API
    
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    # Extract required emotions
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    
    # Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
   