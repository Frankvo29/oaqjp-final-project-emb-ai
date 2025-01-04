import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}

    if text_to_analyze == "":
        return {
            "scores": {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
            },
            "dominant_emotion": None,
            "status_code": 400
        }

    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
        disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
        fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
        joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
        sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]

        scores_dict = {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score,
        }

        dominant_emotion = max(scores_dict, key=scores_dict.get)
    else:
        scores_dict = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
        }
        dominant_emotion = None

    return {
        "scores": scores_dict,
        "dominant_emotion": dominant_emotion,
        "status_code": response.status_code
    }
