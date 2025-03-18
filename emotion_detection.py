import requests

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
headers = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

def get_body(text):
    return  {
        "raw_document": {
            "text": text
        }
    }

def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return {
            "anger": "None",
            "disgust": "None",
            "fear": "None",
            "joy": "None",
            "sadness": "None",
            "dominant_emotion": "None",
        }
    res = requests.post(URL, json=get_body(text_to_analyze), headers = headers)

    emotions = res.json()["emotionPredictions"][0]["emotion"]
    emotions["dominant_emotion"] = max(emotions, key = emotions.get)
    return emotions
