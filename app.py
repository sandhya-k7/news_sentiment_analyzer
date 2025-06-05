import streamlit as st
from news_fetcher import fetch_news
from sentiment_analyzer import analyze_sentiment
from visualizer import show_graph

st.title("📰 News Sentiment Analyzer")

# Input
keyword = st.text_input("Enter keyword", "stock market")
model = st.selectbox("Choose Model", ['VADER (fast)', 'BERT (accurate)', 'RoBERTa (very accurate)'])
graph_type = st.selectbox("Choose Graph", ['Pie Chart', 'Bar Chart', 'Donut Chart', 'Table View'])

if st.button("Run Analysis"):
    if not keyword:
        st.warning("Please enter a keyword.")
    else:
        api_key = "pub_61595988246c485eab2e8cb2233ddf85"
        st.info(f"Fetching news for: **{keyword}**")
        headlines = fetch_news(api_key, keyword)
        if headlines:
            st.success(f"Analyzing {len(headlines)} headlines using {model}")
            df = analyze_sentiment(headlines, model)
            st.dataframe(df)
            show_graph(df, graph_type, streamlit=True)
