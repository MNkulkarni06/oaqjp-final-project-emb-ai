import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers)

    # Convert the response text into a dictionary
    formatted_response = json.loads(response.text)

    # Pull out the emotion scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Find the emotion with the highest score
    dominant_emotion = max(emotions, key=emotions.get)

    # Add it to the dictionary
    emotions['dominant_emotion'] = dominant_emotion

    return emotions