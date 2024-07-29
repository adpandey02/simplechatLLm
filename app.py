
import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from fallback import get_fallback_response
from fallback import objective_words, contains_objective_words
from fallback import BAD_WORDS, contains_bad_words

# prepare response using the fine-tuned model
def result_maker(input_text):
    model = AutoModelForSeq2SeqLM.from_pretrained("./results")
    tokenizer = AutoTokenizer.from_pretrained("./results")
    from transformers import pipeline
    generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
    output = generator(
    input_text,
    max_length=512,  # Set to a high value to allow longer generation
    no_repeat_ngram_size=2,  # To prevent repetitive phrases
    early_stopping=True  # To stop when the model reaches a natural end
    )
    return output[0]['generated_text']
      
# streamlit application
st.title("How can i help you...")


if "messages" not in st.session_state:
  st.session_state.messages = []

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

if prompt := st.chat_input("What is AI?"):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  with st.chat_message("assistant"):
    message_placeholder = st.empty()

    # Check if the user's prompt contains objective words
    if contains_objective_words(prompt, objective_words):
      full_response = get_fallback_response(prompt)
    else:
      full_response = result_maker(prompt)
    # check if original modal response has bad/offensive words, then get response from fallback mechanism
      if contains_bad_words(full_response, BAD_WORDS):
        full_response = get_fallback_response(prompt)

    message_placeholder.markdown(full_response)
  st.session_state.messages.append({"role": "assistant", "content": full_response})