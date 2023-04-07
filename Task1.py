# Task 1 - Given an input string s, find the length of the first longest substring without repeating characters.
# Programmed by - Sheane Jossel Tolentino

import tkinter as tk

def get_longest_substr():
    """
    Description:
        This function finds the longest substring without repeating characters from an input string.
    
    Dependencies:
        This function requires a text field and an output label to be defined in the GUI.
    """

    s = text_field.get()

    # Check if the input string is valid
    if not s.isalpha():
        print("Invalid input. The input should only contain letters and only be one word.")
        exit()

    # Initialize variables for length and contents of the longest substring found
    longest_length = 0
    longest_substring = ""

    # Iterate through all possible substrings of the input string
    for start_ind in range(len(s)):
        visited = set()
        substring = ""
        
        # Iterate over the characters in the current substring
        for end_ind in range(start_ind, len(s)):

            # If the character has not been seen before, add it to the set and the substring
            if s[end_ind] not in visited:
                substring += s[end_ind]
                visited.add(s[end_ind])
                # If the length of the current substring is longer than the longest length found so far, update the longest length
                if len(substring) > longest_length:
                    longest_length = len(substring)
                    longest_substring = substring

            # If a repeating character is encountered, break out of the inner loop and try the next substring
            else:
                break

    output_txt.insert(tk.END, longest_substring)
    output_len.insert(tk.END, longest_length)

# GUI    
root = tk.Tk()
root.title("Task 1")
root.geometry("400x300+10+10")

# Create text field
label = tk.Label(root, text = "Enter a string:")
label.place(x = 100, y = 50)
text_field = tk.Entry(root)
text_field.place(x = 200, y = 50)

# Create a button
button = tk.Button(root, text = "Submit", command=get_longest_substr)
button.place(x = 170, y = 100)

# Create output
output_txtlabel = tk.Label(root, text = "Longest Substring: ")
output_txtlabel.place(x = 90, y = 160)
output_txt = tk.Entry(root)
output_txt.place(x = 200, y = 160)

# Create a label for output
output_lenlabel = tk.Label(root, text = "Length of Longest Substring: ")
output_lenlabel.place(x = 40, y = 210)
output_len = tk.Entry(root)
output_len.place(x = 200, y = 210)

root.mainloop()