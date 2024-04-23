# Mark Montenieri - MS548
# Week 6 project - Estimated time to complete - 2 hours
# Actual time to complete - 20 hours

import pandas as pd
import tkinter as tk
from tkinter import *
from textblob.classifiers import NaiveBayesClassifier
from sklearn.feature_extraction.text import re


def create_sentiment(rating):
    if rating == 1 or rating == 2:
        return -1  # negative sentiment
    elif rating == 4 or rating == 5:
        return 1  # positive sentiment
    else:
        return 0  # neutral sentiment


def clean_data(review):
    no_punc = re.sub(r'[^\w\s]', '', review)
    no_digits = ''.join([i for i in no_punc if not i.isdigit()])

    return (no_digits)


def analyze_text():
    df = pd.read_csv('./tripadvisor_hotel_reviews.csv')
    df.head()
    #print("data: ", df)
    len(df.index)
    df['Sentiment'] = df['Rating'].apply(create_sentiment)
    df['Review'] = df['Review'].apply(clean_data)
    df['Review'][0]

    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidf = TfidfVectorizer(strip_accents=None,
                            lowercase=False,
                            preprocessor=None)

    X = tfidf.fit_transform(df['Review'])
    from sklearn.model_selection import train_test_split
    y = df['Sentiment']  # target variable
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    from sklearn.linear_model import LogisticRegression
    lr = LogisticRegression(solver='liblinear')
    lr.fit(X_train, y_train)  # fit the model
    preds = lr.predict(X_test)  # make predictions

    # Sentiment Analysis
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(preds, y_test)  # 0.86
    print("Accuracy: ", accuracy)
    accuracy_str.set(accuracy)

    # Train Classifier
    cl = NaiveBayesClassifier(train)
    print("Classification", cl.classify("Rating"))
    classification_str.set(cl.classify("Rating"))


train = [('I love this sandwich.', 'pos'),
         ('This is an amazing place!', 'pos'),
         ('I feel very good about these beers.', 'pos'),
         ('This is my best work.', 'pos'),
         ("What an awesome view", 'pos'),
         ('I do not like this restaurant', 'neg'),
         ('I am tired of this stuff.', 'neg'),
         ("I can't deal with this", 'neg'),
         ('He is my sworn enemy!', 'neg'),
         ('My boss is horrible.', 'neg')]

window = tk.Tk()
window.title("Sentiment Analysis of TripAdvisor hotel reviews ")
window.geometry('500x500')

"""
centers a tkinter window
:param window: the main window or Toplevel window to center
"""
window.update_idletasks()
width = window.winfo_width()
frm_width = window.winfo_rootx() - window.winfo_x()
win_width = width + 2 * frm_width
height = window.winfo_height()
titlebar_height = window.winfo_rooty() - window.winfo_y()
win_height = height + titlebar_height + frm_width
x = window.winfo_screenwidth() // 2 - win_width // 2
y = window.winfo_screenheight() // 2 - win_height // 2
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
window.deiconify()

analysis_button = tk.Button(window, text="Analyze Data", command=analyze_text)  # Analyze button
analysis_button.grid(columnspan=2, row=2, padx=5, pady=5)

accuracy_str = tk.StringVar()
accuracy_str.set('')
accuracy_label = tk.Label(window, text="Accuracy")  # Accuracy label
accuracy_label.grid(column=0, row=4, padx=5, pady=5)
accuracy_box = tk.Entry(window)  # Accuracy textbox
# entry.grid(column=1, row=4, padx=5, pady=5)
accuracy_box = Entry(textvariable=accuracy_str, state=DISABLED).grid(column=1, row=4, padx=5, pady=5)

classification_str = tk.StringVar()
classification_str.set('')
classification_label = tk.Label(window, text="Classification")  # Classification label
classification_label.grid(column=0, row=5, padx=5, pady=5)
classification_box = tk.Entry(window)  # Classification textbox
classification_box = Entry(textvariable=classification_str, state=DISABLED).grid(column=1, row=5, padx=5, pady=5)

window.mainloop()
