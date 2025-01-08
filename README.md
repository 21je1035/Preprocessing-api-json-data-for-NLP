# Text Summarization and NLP Preprocessing Dashboard
### Overview
An interactive dashboard where users can input any text. The text undergoes NLP preprocessing steps and is then summarized using an open-source language model available through Hugging Face's transformers library. The dashboard displays the preprocessed text and the generated summary.

### Features 
- Text Input: Users can input any text through the dashboard.
- NLP Preprocessing:
    + Lowercasing: Converts all text to lowercase for consistency.
    + Removing HTML Tags and URLs: Cleans the text by removing any HTML tags and URLs.
    + Removing Punctuation: Strips away punctuation marks from the text.
    + Replacing Chat Abbreviations: Expands common chat abbreviations (e.g., "u" to "you").
    + Removing Stop Words: Eliminates common stop words that do not contribute significant meaning.
    + Converting Emojis to Text: Replaces emojis with their textual descriptions.
    + Tokenization and Lemmatization: Breaks down text into tokens and reduces words to their base form.
- Text Summarization: Uses a pre-trained model (BART) to generate a concise summary of the input text.
- Interactive Dashboard: Built with Streamlit for a user-friendly experience.


### Installation
- Prerequisites
    + Python 3.7 or higher
    + pip package manager

### Steps
1. Clone the Repository
```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.
```
python -m venv venv
```
3. Activate the Virtual Environment

For Windows:
```
venv\Scripts\activate
```
For macOS/Linux:
```
source venv/bin/activate
```
4. Install Dependencies
```
pip install -r requirements.txt
```
5. Download NLTK Data
Run the following commands in a Python shell or add them to your code to download necessary NLTK data.
```
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
```
6. Download SpaCy Model

If not already downloaded, download the English SpaCy model:
```
python -m spacy download en_core_web_sm
```

### Usage
1. Run the Streamlit App
```
streamlit run app.py
```

2. Interact with the Dashboard

- Open the URL provided by Streamlit (usually http://localhost:8501).
- Enter your text in the "Input Text" area.
- Click the "Process" button.
- View the preprocessed text and the summary generated.

### Repository Structure
- 'app.py': Main application file containing the Streamlit dashboard and preprocessing functions.
- 'requirements.txt': Contains all the Python dependencies.
- 'README.md': Project documentation and instructions.
- '.gitignore': Specifies files and directories to be ignored by Git.

### Dependencies
- Python Libraries:
    - streamlit: For creating the interactive dashboard.
    - transformers: Provides access to pre-trained models for summarization.
    - nltk: For natural language processing tasks.
    - spacy: For advanced NLP tasks like tokenization and lemmatization.
    - emoji: For handling emojis in text.
    - torch: Required by transformers for running the models.
    - protobuf<=3.20.1: To avoid compatibility issues with certain versions of transformers and streamlit
 

## Model Selection
- BART Model: The project uses the 'facebook/bart-large-cnn model', which is suitable for summarization tasks.
- Alternative Models:
    - 't5-base': Another transformer model capable of summarization.
    - 'sshleifer/distilbart-cnn-12-6': A smaller, faster model that requires less computational power.

To switch models, modify the summarizer initialization in app.py:
```
from transformers import pipeline

summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base")
```
### Hardware Requirements
- CPU Users:
    - Processing might be slow for large texts.
    - Limit the length of input text to improve performance.
- GPU Users:
    - If available, processing will be significantly faster.
    - Ensure appropriate drivers and CUDA are installed.

### Customization
- Adjusting Summarization Parameters:
  You can adjust max_length and min_length in the get_summary function to control the length of the summary.

- Expanding Chat Abbreviations:
  Add more entries to the chat_words dictionary in app.py to handle additional abbreviations.

### Error Handling
- The app includes basic error handling to manage exceptions during summarization.
- If an error occurs, it will be displayed in the Streamlit app.
