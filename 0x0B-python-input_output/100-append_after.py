#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """
    the func inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, mode='r+', encoding="utf-8") as f:
        new_list = []
        for line in f:
            new_list.append(line)
            if search_string in line:
                new_list.append(new_string)
        f.seek(0)
        f.writelines(new_list)
