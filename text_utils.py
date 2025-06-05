import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def clean_text(text):
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    return " ".join([w for w in words if w.lower() not in stop_words])
