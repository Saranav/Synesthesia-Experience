def sentiment_to_colour(sentiment):
    """Map sentiment polarity to a basic colour."""
    if sentiment > 0:
        return "Green (Positive)"
    elif sentiment < 0:
        return "Red (Negative)"
    else:
        return "Blue (Neutral)"

def simple_sentiment_analysis(sentence):
    """A very basic sentiment analysis using keyword matching."""
    positive_words = ['happy', 'joy', 'love', 'bright', 'hope']
    negative_words = ['sad', 'pain', 'angry', 'dark', 'fear']

    
    # Count positive and negative words
    sentiment_score = 0
    words = sentence.lower().split()
    
    for word in words:
        if word in positive_words:
            sentiment_score += 1
        elif word in negative_words:
            sentiment_score -= 1
    
    # Return sentiment score
    return sentiment_score

def analyze_text(text):
    """Analyze each sentence in the text."""
    sentences = text.split('.')
    
    for sentence in sentences:
        if sentence.strip():  # Only process non-empty sentences
            sentiment = simple_sentiment_analysis(sentence)
            colour = sentiment_to_colour(sentiment)
            print(f"Sentence: \"{sentence.strip()}\"")
            print(f"Sentiment score: {sentiment}, Colour: {colour}")
            print()



# Example text input (poem)
text = """
The sky is bright and full of hope.
But darkness surrounds me with fear.
Love guides me forward.
I am angry and lost in the night.
"""

# Run the analysis
analyze_text(text)
