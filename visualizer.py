import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def show_graph(df, graph_type):
    sentiment_counts = df['Sentiment'].value_counts()
    colors = ['#28a745', '#dc3545', '#6c757d']
    explode = (0.05, 0.05, 0.05)

    if graph_type == 'Table View':
        st.dataframe(df)

    elif graph_type == 'Pie Chart':
        fig, ax = plt.subplots()
        ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%',
               startangle=140, colors=colors, explode=explode, shadow=True)
        ax.axis('equal')
        st.pyplot(fig)

    elif graph_type == 'Donut Chart':
        fig, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(sentiment_counts, labels=sentiment_counts.index,
                                          autopct='%1.1f%%', startangle=140, colors=colors,
                                          explode=explode, shadow=True)
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        ax.add_artist(centre_circle)
        ax.axis('equal')
        st.pyplot(fig)

    elif graph_type == 'Bar Chart':
        fig, ax = plt.subplots()
        sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values,
                    palette=colors, ax=ax)
        ax.set_title("Sentiment Count by Category")
        for i, v in enumerate(sentiment_counts.values):
            ax.text(i, v + 0.2, str(v), ha='center')
        st.pyplot(fig)
