
import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

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


st.title("How can i help you...")


# if "openai_model" not in st.session_state:
#   st.session_state["openai_model"] = "gpt-3.5-turbo"

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
    full_response = result_maker(prompt)

    # for response in openai.ChatCompletion.create(
    #   model=st.session_state["openai_model"],
    #   messages=[
    #     {"role": m["role"], "content": m["content"]}
    #     for m in st.session_state.messages
    #   ],
    #   stream=True,
    # ):
    #   full_response += response.choices[0].delta.get("content", "")
    #   message_placeholder.markdown(full_response + "▌")
    message_placeholder.markdown(full_response)
  st.session_state.messages.append({"role": "assistant", "content": full_response})