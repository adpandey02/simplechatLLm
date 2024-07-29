from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables
import os
import google.generativeai as genai
objective_words = ['hello', 'you', 'can you']
BAD_WORDS = ['kill', 'sex', 'slave']

# class fallback():

def get_fallback_response(prompt):
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    response = genai.chat(messages=[prompt]) 
    return response.last

def contains_objective_words(text, objective_words):
    
    """Check if the text contains any objective words."""
    for word in objective_words:
        if word.lower() in text.lower():
            return True
    return False

def contains_bad_words(text, bad_words):
    
    """Check if the text contains any bad words."""
    for word in bad_words:
        if word.lower() in text.lower():
            return True
    return False

