"""
Text Generator Module
Generates sentiment-aligned text using GPT-2
"""

from transformers import pipeline
import torch

class TextGenerator:
    def __init__(self):
        """Initialize the text generation pipeline"""
        self.generator = pipeline(
            "text-generation",
            model="gpt2-medium",  # Better quality than base gpt2
            device=0 if torch.cuda.is_available() else -1
        )
        
        # Sentiment-specific prompt templates
        self.sentiment_prompts = {
            'positive': [
                "This is wonderful because",
                "I'm so happy that",
                "The best thing about this is",
                "It's amazing how",
                "I love the way"
            ],
            'negative': [
                "This is disappointing because",
                "I'm frustrated that",
                "The worst part is",
                "Unfortunately,",
                "I dislike how"
            ],
            'neutral': [
                "It is worth noting that",
                "One could say that",
                "From an objective perspective,",
                "The fact is that",
                "Considering this,"
            ]
        }
    
    def generate(self, prompt, sentiment, max_length=150, temperature=0.8):
        """
        Generate text based on prompt and sentiment
        
        Args:
            prompt (str): User's input prompt
            sentiment (str): 'positive', 'negative', or 'neutral'
            max_length (int): Maximum length of generated text
            temperature (float): Creativity (0.7-1.0 recommended)
            
        Returns:
            str: Generated text
        """
        # Create sentiment-conditioned prompt
        sentiment_prefix = self._get_sentiment_prefix(sentiment)
        full_prompt = f"{sentiment_prefix} {prompt}"
        
        # Generate text
        result = self.generator(
            full_prompt,
            max_length=max_length,
            num_return_sequences=1,
            temperature=temperature,
            top_p=0.9,
            do_sample=True,
            pad_token_id=self.generator.tokenizer.eos_token_id
        )
        
        # Extract generated text
        generated_text = result[0]['generated_text']
        
        # Clean up: remove the prompt prefix if needed
        return generated_text
    
    def _get_sentiment_prefix(self, sentiment):
        """Get a random sentiment-appropriate prefix"""
        import random
        sentiment = sentiment.lower()
        
        if sentiment in self.sentiment_prompts:
            return random.choice(self.sentiment_prompts[sentiment])
        else:
            return random.choice(self.sentiment_prompts['neutral'])
    
    def generate_paragraph(self, prompt, sentiment, num_sentences=5):
        """
        Generate a full paragraph with multiple sentences
        
        Args:
            prompt (str): User's input prompt
            sentiment (str): Desired sentiment
            num_sentences (int): Approximate number of sentences
            
        Returns:
            str: Generated paragraph
        """
        # Estimate tokens (roughly 20 tokens per sentence)
        estimated_length = num_sentences * 20 + len(prompt.split())
        
        return self.generate(
            prompt=prompt,
            sentiment=sentiment,
            max_length=min(estimated_length, 200),
            temperature=0.8
        )