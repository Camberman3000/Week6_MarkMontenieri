# Mark Montenieri - MS548
# Week 3 project - Estimated time to complete - 2 hours
# Actual time to complete - 2 hours
# from textblob lib import TextBlob method
from textblob import TextBlob


def task_textblob_sentiment():
    # perform sentiment analysis using textblob
    text = input("Type a sentence to analyze, which will return the sentiment (Higher polarity = more positive & "
                 "Higher subjectivity = more opinionated): ")
    blob = TextBlob(text)
    sentiment_result = blob.sentiment
    print("Sentiment analysis results: " + str(sentiment_result))
    outfile = open("output.txt", "a")  # Open file
    outfile.write("Menu option 4 (Sentiment) output: ")  # Write to file
    outfile.write(str(sentiment_result) + "\n")  # Write product to file
    outfile.close()  # Close the file
    menu_loop()


def menu_loop():  # Main menu
    try:
        print("\nWelcome to Mark's Sentiment Analysis Python Project.")
        print("Menu")
        print("1. Perform Analysis")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")
        if choice.isdigit() and 1 <= int(choice) <= 2:
            choice = int(choice)
            if choice == 1:
                task_textblob_sentiment()
            elif choice == 2:
                print("Exiting program")
                quit()
        else:
            print("Invalid choice. Please choose a number between 1 and 2")
            menu_loop()  # Reload Menu
    except TypeError:
        print("Try Exception")


if __name__ == "__main__":
    menu_loop()  # Load Menu
