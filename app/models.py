from transformers import pipeline

try:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    generator = pipeline("text-generation", model="gpt2")
except Exception as e:
    print("Failed to load models: {}".format(e))
