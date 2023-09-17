# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 23:54:38 2023

@author: USER
"""

import re
import nltk
from textblob import TextBlob
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
# Class which describes Ai hirring asistent with sentiment
class HirringAsistent:
    # Define list of stop words to remove from text
    stop_words = set(stopwords.words('english'))
    
    # Define lemmatizer to reduce words to their base form
    lemmatizer = WordNetLemmatizer()    
    
    # Define function to clean text and remove stop words
    def clean_text(self, text):
        # Remove non-alphanumeric characters
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        # Tokenize text into individual words
        tokens = word_tokenize(text.lower())
        # Remove stop words from tokens
        filtered_tokens = [word for word in tokens if word not in self.stop_words]
        # Lemmatize filtered tokens
        lemmatized_tokens = [self.lemmatizer.lemmatize(token) for token in filtered_tokens]
        # Return cleaned text as a string
        return ' '.join(lemmatized_tokens)
    
    # Define list of inclusive keywords to search for in cleaned text
    inclusive_keywords = ['equal opportunity', 'diversity', 'inclusion',
                          'minority', 'gender', 'race', 'ethnicity', 'sexual orientation']
    
    # Define function to get inclusive score for a given job description
    def get_inclusive_score(self, description):
        # Clean job description text
        cleaned_text = self.clean_text(description)
        # Split cleaned text into individual words
        words = cleaned_text.split()
        # Calculate total number of words in job posting
        total_words = len(words)
        # Calculate number of occurrences of each inclusive keyword
        keyword_counts = [words.count(keyword.lower()) for keyword in self.inclusive_keywords]
        # Calculate total number of inclusive keywords
        total_keywords = sum(keyword_counts)
        # Calculate inclusive score as a percentage of total words
        inclusive_score = total_keywords / total_words * 100
        return inclusive_score
    
    # Define function to get sentiment score for a given job description
    def get_sentiment_score(self, description):
        cleaned_text = self.clean_text(description)
        # Get TextBlob object for cleaned text
        blob = TextBlob(cleaned_text)
        # Calculate sentiment score using TextBlob
        sentiment_score = blob.sentiment.polarity
        return sentiment_score
    

