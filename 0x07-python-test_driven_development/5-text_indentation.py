#!/usr/bin/python3

def text_indentation(text):
    """Prints a text with 2 new lines after
        each of these characters: ., ? and :
    Args:
        text (str): text to print
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = ""
    for i in text:
        new_text += i
        if i in ".?:":
            new_text += "\n\n"
    print("\n".join([line.strip() for line in new_text.split("\n")]), end="")
