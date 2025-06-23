from transformers import pipeline

# Load Hugging Face NER pipeline
ner_pipeline = pipeline(
    "ner",
    model="dbmdz/bert-large-cased-finetuned-conll03-english",
    aggregation_strategy="simple"
)

def extract_entities(text: str):
    """
    Extract named entities from a given text.
    """
    if not text or not text.strip():
        return []
    return ner_pipeline(text)