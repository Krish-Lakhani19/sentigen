from src.text_generator import TextGenerator

# Initialize generator (this will download gpt2-medium ~1.5GB)
print("Loading text generator...")
generator = TextGenerator()
print("✅ Generator loaded!\n")

# Test with different sentiments
test_cases = [
    ("summer vacation", "positive"),
    ("the movie ending", "negative"),
    ("artificial intelligence", "neutral")
]

for prompt, sentiment in test_cases:
    print(f"Prompt: '{prompt}' | Sentiment: {sentiment}")
    print("-" * 60)
    
    generated = generator.generate_paragraph(prompt, sentiment, num_sentences=3)
    print(generated)
    print("\n" + "=" * 60 + "\n")