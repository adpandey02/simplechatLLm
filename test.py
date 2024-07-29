from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load the model
model = AutoModelForSeq2SeqLM.from_pretrained("./results")

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("./results")

# Now you can use the model and tokenizer for inference
from transformers import pipeline

# Create a pipeline for text generation
generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

# Example input text
input_text = "what are your views on advancement in AI"

# Generate the output
output = generator(
    input_text,
    max_length=512,  # Set to a high value to allow longer generation
    no_repeat_ngram_size=2,  # To prevent repetitive phrases
    early_stopping=True  # To stop when the model reaches a natural end
)

# Print the output
print(output)
