import gradio as gr

def run_sentiment(keyword, model_choice, graph_type):
    headlines = fetch_news(api_key, keyword)
    df = analyze_sentiment(headlines, model_choice)
    return df  # or plot or both

gr.Interface(
    fn=run_sentiment,
    inputs=[
        gr.Textbox(label="Keyword"),
        gr.Dropdown(['VADER (fast)', 'BERT (accurate)', 'RoBERTa (very accurate)']),
        gr.Dropdown(['Pie Chart', 'Bar Chart', 'Donut Chart', 'Table View'])
    ],
    outputs="dataframe"
).launch()
