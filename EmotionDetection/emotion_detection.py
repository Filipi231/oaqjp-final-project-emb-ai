"""Detecção de emoções usando o serviço Watson NLP (EmotionPredict)."""
import requests

URL = ("https://sn-watson-emotion.labs.skills.network/v1/"
       "watson.runtime.nlp.v1/NlpService/EmotionPredict")
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyse):
    """Analisa o texto e retorna as pontuações de emoção e a emoção dominante.

    Em caso de texto vazio ou status 400 do serviço, todos os valores são None
    e status_code é 400.
    """
    error_result = {emotion: None for emotion in EMOTIONS}
    error_result.update({"dominant_emotion": None, "status_code": 400})

    if not text_to_analyse or not text_to_analyse.strip():
        return error_result

    payload = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(URL, json=payload, headers=HEADERS, timeout=30)

    if response.status_code == 400:
        return error_result

    emotions = response.json()["emotionPredictions"][0]["emotion"]
    result = {emotion: emotions[emotion] for emotion in EMOTIONS}
    result["dominant_emotion"] = max(result, key=result.get)
    result["status_code"] = response.status_code
    return result
