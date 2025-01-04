import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    emotion_predictions = formatted_response["emotionPredictions"][0]

    anger_score = emotion_predictions["emotion"]["anger"]
    disgust_score = emotion_predictions["emotion"]["disgust"]
    fear_score = emotion_predictions["emotion"]["fear"]
    joy_score = emotion_predictions["emotion"]["joy"]
    sadness_score = emotion_predictions["emotion"]["sadness"]

    scores_dict = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
    }
    dominant_emotion = max(scores_dict, key=scores_dict.get)
    
    return {
        "scores": scores_dict,
        "dominant_emotion": dominant_emotion,
    }
    