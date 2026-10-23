"""Aplicação Flask para detecção de emoções."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """Exibe a página inicial."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emot_detector():
    """Recebe textToAnalyze e devolve a resposta formatada."""
    text = request.args.get("textToAnalyze", "")
    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return "Texto inválido! Por favor, tente novamente!"

    return (
        f"Para a declaração dada, a resposta do sistema é 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} e 'sadness': {result['sadness']}. "
        f"A emoção dominante é {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
