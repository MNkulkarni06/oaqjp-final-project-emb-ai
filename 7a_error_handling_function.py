"""Emotion detection using the Watson NLP library."""
import json
import requests


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion for the given text."""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers, timeout=30)

    # Blank or invalid input returns status code 400
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    emotions['dominant_emotion'] = max(emotions, key=emotions.get)

    return emotions