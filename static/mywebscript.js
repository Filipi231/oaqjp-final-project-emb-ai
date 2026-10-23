function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const output = document.getElementById("system_response");

    fetch("/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze))
        .then((response) => response.text())
        .then((text) => {
            output.textContent = text;
        })
        .catch(() => {
            output.textContent = "Erro ao contatar o servidor.";
        });
}
