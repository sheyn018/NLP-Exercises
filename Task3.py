# Task 3 - Sentence Combination
# Programmed by - Sheane Jossel Tolentino

import tkinter as tk
import spacy

nlp = spacy.load("en_core_web_sm")

def combine_sentences():
    """
    Description:
        Combines two sentences into a single sentence based on the relationship between their main verbs and predicates.

    Args:
        sentence1 (str): The first sentence to be combined.
        sentence2 (str): The second sentence to be combined.

    Returns:
        combined_sentence (str): The combined sentence.
    """

    sentence1 = text_field1.get()
    sentence2 = text_field2.get()

    # Parse the sentences using spaCy
    doc1 = nlp(sentence1)
    doc2 = nlp(sentence2)

    # Find the root of each sentence (the main verb or predicate)
    root1 = [token for token in doc1 if token.head == token][0]
    root2 = [token for token in doc2 if token.head == token][0]

    # Combine the sentences based on the relationship between the roots
    if root1.dep_ == "ROOT" and root2.dep_ == "ROOT":
        # If both roots are main verbs, combine the sentences using a coordinating conjunction
        combined_sentence = f"{sentence1} and {sentence2}"
    elif root1.dep_ == "ROOT" and root2.dep_ != "ROOT":
        # If the first sentence has a main verb and the second does not, combine the sentences using the object of the first sentence
        combined_sentence = f"{sentence1} {doc2[root2.i+1:].text}"
    elif root1.dep_ != "ROOT" and root2.dep_ == "ROOT":
        # If the second sentence has a main verb and the first does not, combine the sentences using the subject of the second sentence
        combined_sentence = f"{doc1[:root1.i].text} {sentence2}"
    else:
        # If both sentences have non-root verbs, combine the sentences using the subject of the second sentence and the object of the first sentence
        combined_sentence = f"{doc1[:root1.i].text} {doc2[root2.i+1:].text}"
    
    # Create a label for output
        output_label = tk.Label(root, text="Sorted Sentences Based on Information Density")
        output_label.pack(padx=20, pady=10)

    # Create the scrollbar widget
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create the text widget for the output
    output = tk.Text(root, yscrollcommand=scrollbar.set)
    output.pack()
    
    # Configure the scrollbar to work with the text widget
    scrollbar.config(command=output.yview)

    # Insert the sentence into the text widget
    output.insert(tk.END, combined_sentence)
    
# GUI    
root = tk.Tk()
root.title("Task 3")
root.geometry("480x360")

# Create a first label and first text field
label1 = tk.Label(root, text = "Enter first sentence:")
label1.pack(padx = 20, pady = 10)
text_field1 = tk.Entry(root, width = 30)
text_field1.pack(padx = 20, pady = 10)

# Create a second label and second text field
label2 = tk.Label(root, text = "Enter second sentence:")
label2.pack(padx = 20, pady = 10)
text_field2 = tk.Entry(root, width = 30)
text_field2.pack(padx = 20, pady = 10)

# Create a button
button = tk.Button(root, text = "Submit", command=combine_sentences)
button.pack(padx = 20, pady = 10)

root.mainloop()