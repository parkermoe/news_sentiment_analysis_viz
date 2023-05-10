import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load the BERT model for sentiment analysis
tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

def get_sentiment(text):
    # Truncate or pad the input text to fit within the model's maximum input length
    inputs = tokenizer.encode(text, return_tensors="pt", max_length=512, truncation=True, padding='max_length')
    
    # Get the model's output
    outputs = model(inputs)[0]
    
    # Obtain the sentiment prediction
    _, prediction = torch.max(outputs, 1)
    prediction_index = prediction.item()
    
    if prediction_index > 2:  # Ensure the index is within the expected range
        prediction_index = 2
    
    sentiment = ["negative", "neutral", "positive"][prediction_index]
    return sentiment

def apply_sentiment_analysis(df):
    # Apply sentiment analysis to the DataFrame
    df["sentiment"] = df["content"].apply(get_sentiment)
    return df
