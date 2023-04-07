# Task 2 - Information Density Sentence Sorting
# Programmed by - Sheane Jossel Tolentino

import string
import tkinter as tk
from tkinter import filedialog
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def get_info_density(sentence):
    """
    Description:
        Calculates the information density of a sentence by dividing the number of unique non-stopwords by the total number of non-stopwords.

    Args:
        sentence (str): The sentence to calculate the information density for.

    Returns:
        float: The information density of the sentence.
    """

    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in word_tokenize(sentence) if word.lower() not in stop_words and word.lower() not in string.punctuation]
    unique_words = set(words)
    return len(unique_words) / len(words)

def sort_sentences(text):
    """
    Description:
        Sorts the sentences in a text by their information density.

    Args:
        text (str): The text to sort.

    Returns:
        list: A list of sentences sorted by their information density in descending order.
    """

    sentences = sent_tokenize(text)
    sentence_info_densities = [(sentence, get_info_density(sentence)) for sentence in sentences]
    sorted_sentences = [sentence for sentence, _ in sorted(sentence_info_densities, key=lambda x: x[1], reverse=True)]

    return sorted_sentences

def open_display():
    """
    Description:
        Opens a file dialog to allow the user to select a text file, reads the contents of the file, 
        sorts the sentences in the text by information density, and displays the sorted sentences in a 
        text widget with a scrollbar.
    """

    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    # Check if the user has selected a file
    if filename:
        with open(filename, 'r') as file:
            text = file.read()
        
        # Create a label for output
        sentences_label = tk.Label(root, text="Sorted Sentences Based on Information Density")
        sentences_label.pack(padx=20, pady=10)

        # Create the scrollbar widget
        scrollbar = tk.Scrollbar(root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create the text widget for the sentences
        sentences_text = tk.Text(root, yscrollcommand=scrollbar.set)
        sentences_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configure the scrollbar to work with the text widget
        scrollbar.config(command=sentences_text.yview)

        # Sort the sentences in the text by information density
        sorted_sentences = sort_sentences(text)

        # Create a list of formatted sentence strings
        sentences_list = []
        for index, sentence in enumerate(sorted_sentences):
            sort_sen = f"Sentence {index + 1}: \n{sentence}\n\n"
            sentences_list.append(sort_sen)

        # Insert the sentences into the text widget
        sentences_text.insert(tk.END, "".join(sentences_list))

    else:
        print("\nNo file selected. Program exited.")

# GUI
root = tk.Tk()
root.title("Task 2")
root.geometry("720x480")

# Create instruction label
instruction_label = tk.Label(root, text="Click the button below to open a text file. \nTXT files are the only files you can select")
instruction_label.pack(padx = 20, pady = 10)

# Create button
button = tk.Button(root, text="Open File", command=open_display)
button.pack(padx = 20, pady = 10)

root.mainloop()