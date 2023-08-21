import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import streamlit as st

# Load the CSV dataset into a Pandas DataFrame
csv_file_path = 'socialmedia.csv'
df = pd.read_csv(r'C:\Users\Hp\Downloads\socialmedia.csv')

# Data Preprocessing
df['User Description 1'] = df['User Description 1'].str.lower()
df['User Description 2'] = df['User Description 2'].str.lower()
df['Post Text'] = df['Post Text'].str.lower()

# Sentiment Analysis using TextBlob
def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

df['sentiment'] = df['Post Text'].apply(get_sentiment)

# User Engagement Analysis
numerical_engagement_columns = ['User ID', 'Likes/Reactions', 'Shares/Retweets', 'Comments']
df['total_engagement'] = df[numerical_engagement_columns].sum(axis=1)

# Streamlit App
st.title('Social Media Analysis')

# Sentiment Analysis Visualization
st.subheader('Sentiment Analysis')
plt.figure(figsize=(8, 5))
df['sentiment'].hist(bins=20, color='blue', alpha=0.7)
plt.title('Sentiment Analysis')
plt.xlabel('Sentiment Polarity')
plt.ylabel('Frequency')
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

# User Engagement Analysis Visualization
st.subheader('User Engagement Analysis')
plt.figure(figsize=(8, 5))
df.plot(y='total_engagement', kind='line', color='green', marker='o')
plt.title('User Engagement Analysis')
plt.ylabel('Total Engagement')
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

