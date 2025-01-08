
# Install necessary packages
# Uncomment the following line if running for the first time
# !pip install streamlit transformers nltk spacy emoji

# Import necessary libraries
import streamlit as st

# Load necessary NLP models and download corpora
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
import spacy
try:
    nlp = spacy.load('en_core_web_sm')
except:
    spacy.cli.download('en_core_web_sm')
    nlp = spacy.load('en_core_web_sm')
from nltk.stem import WordNetLemmatizer

# Import summarization pipeline from transformers
from transformers import pipeline

# Initialize summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  # You can choose other models too

# Function definitions for preprocessing
def cleanhtml(raw_html):
    import re
    CLEANR = re.compile('<.*?>')
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext

def remove_url(text):
    import re
    pattern = re.compile(r'https?://\S+|www\.\S+')
    return pattern.sub(r'', text)

def remove_punct(text):
    import string
    return text.translate(str.maketrans('', '', string.punctuation))

def replace_short_forms(text):
    chat_words = {
        "afaik": "as far as i know",
        "afk": "away from keyboard",
        "asap": "as soon as possible",
        # ... [Include all your entries in lowercase]
        "ttyl": "talk to you later",
        "u": "you",
        "u2": "you too",
        # Add the rest of your chat words here...
    }
    for short_form, long_form in chat_words.items():
        text = text.replace(short_form, long_form)
    return text

def remove_stopwords(text):
    from nltk.corpus import stopwords
    return ' '.join(word for word in text.split() if word not in stopwords.words('english'))

def remove_emojis(text):
    import emoji
    return emoji.demojize(text)

def tokenizer(text):
    doc = nlp(text)
    return [token.lemma_ for token in doc]

def lemmatizing(tokens):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]

# Pipeline function for preprocessing
def preprocessing_pipeline(text):
    # Convert to lowercase
    text = text.lower()
    # Remove HTML tags
    text = cleanhtml(text)
    # Remove URLs
    text = remove_url(text)
    # Remove punctuation
    text = remove_punct(text)
    # Replace chat words
    text = replace_short_forms(text)
    # Remove stopwords
    text = remove_stopwords(text)
    # Remove emojis
    text = remove_emojis(text)
    # Tokenization
    tokens = tokenizer(text)
    # Lemmatization
    tokens = lemmatizing(tokens)
    # Rejoin tokens into a string
    text = ' '.join(tokens)
    return text

# Function to get summary using transformers
def get_summary(text):
    # The summarizer expects text of a certain length due to token limitations
    max_chunk = 500
    text = text.strip().replace("\n", " ")
    # Split the text into chunks if it's too long
    paragraphs = []
    while len(text) > max_chunk:
        idx = text.rfind('.', 0, max_chunk)
        if idx == -1:
            idx = max_chunk
        paragraphs.append(text[:idx+1])
        text = text[idx+1:]
    paragraphs.append(text)
    # Summarize each chunk and combine the summaries
    summaries = []
    for paragraph in paragraphs:
        summary = summarizer(paragraph, max_length=130, min_length=30, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    return ' '.join(summaries)

# Create Streamlit dashboard
def main():
    st.title("Text Summarization and NLP Preprocessing Dashboard")
    st.write("Enter your text below for preprocessing and summarization:")
    
    user_input = st.text_area("Input Text", "", height=200)
    
    if st.button("Process"):
        if user_input.strip():
            with st.spinner('Processing...'):
                # Preprocessing
                preprocessed_text = preprocessing_pipeline(user_input)
                # Summarization
                try:
                    summary = get_summary(preprocessed_text)
                except Exception as e:
                    st.error(f"An error occurred during summarization: {e}")
                    return
                
            # Display results
            st.subheader("Preprocessed Text")
            st.write(preprocessed_text)
            
            st.subheader("Summary")
            st.write(summary)
        else:
            st.warning("Please enter text to process.")

if __name__ == "__main__":
    main()