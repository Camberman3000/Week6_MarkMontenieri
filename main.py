# Mark Montenieri - MS548
# Week 3 project - Estimated time to complete - 2 hours
# Actual time to complete - 2 hours
# from textblob lib import TextBlob method
import urllib.request
from nltk import NaiveBayesClassifier as nbc
from nltk.tokenize import word_tokenize
from itertools import chain

import nltk
import tkinter as tk
from tkinter import *



def document_features(document):
    words = set(document)
    doc_features = {}
    for word in word_features:
        doc_features[f'contains({word})'] = (word in words)
        return doc_features

def analyze_text():
    data = urllib.request.urlopen("https://www.google.com/").read(20000)  # read only 20 000 chars
    data = data.decode('utf-8')
    #print("data: ", data)

    all_words = nltk.FreqDist(w.lower() for w in data)
    word_features = list(all_words.keys())[:2000]
    featuresets = [(document_features(d), c) for (d, c) in data[1, 2]]
    train_set, test_set = featuresets[1000:], featuresets[:1000]

    #  Train a Naive Bayes classifier
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    # Accuracy
    accuracy = nltk.classify.accuracy(classifier, test_set)
    print("Accuracy: ", accuracy)

    example_text = "This Movie is bad"
    features = document_features(example_text.split())
    print("Classification: ", classifier.classify(features))



train_set = [('I love this sandwich.', 'pos'),
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
window.title("Sentiment Analysis - Please choose a website URL containing an article")
window.geometry('500x500')

# window.eval('tk::PlaceWindow . center')

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

analysis_button = tk.Button(window, text="Analyze URL", command=analyze_text)  # Analyze button
analysis_button.grid(columnspan=2, row=2, padx=5, pady=5)

url_label = tk.Label(window, text="URL")  # URL Label
url_label.grid(column=0, row=3, padx=5, pady=5)
url_box = tk.Entry(window)  # URL textbox
url_box.grid(column=1, row=3, padx=5, pady=5)

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
