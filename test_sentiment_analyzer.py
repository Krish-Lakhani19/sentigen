from src.sentiment_analyzer import SentimentAnalyzer
analyser=SentimentAnalyzer()
test_texts={
    "I absolutely love this wonderful day!",
    "This is terrible and disappointing.",
    "The weather is okay, nothing special."
}
for text in test_texts:
    result=analyser.analyze(text)
    print(f"Text:{text}")
    print(f"Result:{result}\n")