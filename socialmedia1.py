import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import streamlit as st

# Sentiment Analysis using TextBlob
def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

# Streamlit App
st.title('Social Media Analysis')

# File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the CSV dataset into a Pandas DataFrame
    df = pd.read_csv(uploaded_file)

    # Data Preprocessing
    df['Post Text'] = df['Post Text'].str.lower()

    # Sentiment Analysis
    df['sentiment'] = df['Post Text'].apply(get_sentiment)

    # User Engagement Analysis
    numerical_engagement_columns = ['User ID', 'Likes/Reactions', 'Shares/Retweets', 'Comments']
    df['total_engagement'] = df[numerical_engagement_columns].sum(axis=1)

    # Interactive Filtering
    sentiment_range = st.slider("Select Sentiment Polarity Range", -1.0, 1.0, (-1.0, 1.0))
    filtered_df = df[(df['sentiment'] >= sentiment_range[0]) & (df['sentiment'] <= sentiment_range[1])]

    # Display Data Table
    st.subheader('Filtered Data')
    st.write(filtered_df)

    # Sentiment Analysis Visualization
    st.subheader('Sentiment Analysis')
    plt.figure(figsize=(8, 5))
    filtered_df['sentiment'].hist(bins=20, color='blue', alpha=0.7)
    plt.title('Sentiment Analysis')
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Frequency')
    st.pyplot()

    # User Engagement Analysis Visualization
    st.subheader('User Engagement Analysis')
    plt.figure(figsize=(8, 5))
    filtered_df.plot(y='total_engagement', kind='line', color='green', marker='o')
    plt.title('User Engagement Analysis')
    plt.ylabel('Total Engagement')
    st.pyplot()
