import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline
from text_utils import clean_text

from transformers import pipeline
import streamlit as st

@st.cache_resource
def load_bert_model():
    return pipeline("sentiment-analysis")

@st.cache_resource
def load_roberta_model():
    return pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")


def analyze_sentiment(headlines, model_name):
    results = []

    if model_name == 'VADER (fast)':
        analyzer = SentimentIntensityAnalyzer()
        for headline in headlines:
            cleaned = clean_text(headline)
            score = analyzer.polarity_scores(cleaned)['compound']
            sentiment = 'Positive' if score >= 0.05 else 'Negative' if score <= -0.05 else 'Neutral'
            results.append({'Headline': headline, 'Sentiment': sentiment})

    elif model_name == 'BERT (accurate)':
        bert_analyzer = pipeline("sentiment-analysis")
        for headline in headlines:
            result = bert_analyzer(headline)[0]
            sentiment = result['label'].capitalize()
            results.append({'Headline': headline, 'Sentiment': sentiment})

    elif model_name == 'RoBERTa (very accurate)':
        roberta_analyzer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
        for headline in headlines:
            result = roberta_analyzer(headline)[0]
            label = result['label']
            label_map = {
                'LABEL_0': 'Negative',
                'LABEL_1': 'Neutral',
                'LABEL_2': 'Positive'
            }
            sentiment = label_map.get(label, label)
            results.append({'Headline': headline, 'Sentiment': sentiment})

    return pd.DataFrame(results)
