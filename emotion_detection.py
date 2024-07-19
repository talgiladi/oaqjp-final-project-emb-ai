import requests
def emotion_detector(text_to_analyse):    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_body = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers=headers, json=json_body)
    dic = response.json()
    dominantEmotion = ""
    dominantScore = -1
    for i, key in dic.keys():
        if dic[key]["score"] > dominantScore:
            dominantScore = dic[key]["score"]
            dominantEmotion = dic[key]["emotion"]
    
    result = {
        'anger': dic["anger"]["score"],
        'disgust': dic["disgust"]["score"],
        'fear': dic["fear"]["score"],
        'joy': dic["joy"]["score"],
        'sadness': dic["sadness"]["score"],
        'dominant_emotion': dominantEmotion
        }
    return result


    

