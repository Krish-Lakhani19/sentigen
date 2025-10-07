"""
Sentiment Analyzer Module
Uses pre-trained transformer model to detect sentiment in text
"""

from transformers import pipeline
import torch

class SentimentAnalyzer:
    def __init__(self):
        """Initialize the sentiment analysis pipeline"""
        self.analyzer = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english",
            device=0 if torch.cuda.is_available() else -1
        )
    
    def analyze(self, text):
        """
        Analyze sentiment of input text
        
        Args:
            text (str): Input text to analyze
            
        Returns:
            dict: Contains 'sentiment' (POSITIVE/NEGATIVE) and 'confidence'
        """
        result = self.analyzer(text)[0]
        return {
            'sentiment': result['label'],
            'confidence': round(result['score'], 4)
        }
    
    def get_sentiment_label(self, text):
        """
        Get simple sentiment label: positive, negative, or neutral
        
        Args:
            text (str): Input text
            
        Returns:
            str: 'positive', 'negative', or 'neutral'
        """
        analysis_result = self.analyze(text)
        
        if analysis_result['confidence'] < 0.6:
            return 'neutral'
        
        return analysis_result['sentiment'].lower()