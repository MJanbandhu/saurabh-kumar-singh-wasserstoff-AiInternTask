from textblob import TextBlob

def summarize_attributes(identified_objects, extracted_texts):
    summaries = []
    for obj, text in zip(identified_objects, extracted_texts):
        description = f"Object: {obj['label']}, Confidence: {obj['confidence']}"
        combined_text = f"{description}. {text}"
        blob = TextBlob(combined_text)
        
        # Handle cases where there might be no sentences
        summary = str(blob.sentences[0]) if blob.sentences else combined_text
        summaries.append(summary)
    
    return summaries

# Example usage
if __name__ == "__main__":
    identified_objects = [{'label': 'dog', 'confidence': 0.85}, {'label': 'car', 'confidence': 0.92}]
    extracted_texts = ["License plate: ABC123.", "Brand: Tesla."]
    summaries = summarize_attributes(identified_objects, extracted_texts)
    
    # Print summaries for verification
    for summary in summaries:
        print(summary)