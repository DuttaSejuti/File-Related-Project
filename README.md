# File-Related-Project
This is a project done for one of the Courseras' courses of Python under Rice University

# Problem 1: Finding the first difference between two lines (singleline_diff function)
First, you will write a function called singleline_diff that takes two single line strings. You may assume that both strings are always a single line and do not contain any newline characters. The function should return the index of the first character that differs between the two lines.  If the lines are the same, the function should return the constant IDENTICAL, which is already defined to be -1−1 in the provided template file.

# Problem 2: Presenting the differences between two lines in a nicely formatted way (singleline_diff_format function)
Next, you will write a function called singleline_diff_format that takes two single line strings and the index of the first difference and will generate a formatted string that will allow a user to clearly see where the first difference between two lines is located. A user is likely going to want to see where the difference is in the context of the lines, not just see a number. Your function will return a three line string that looks as follows:

abcd <br />
==^ <br />
abef <br />

# Problem 3: Finding the first difference across multiple lines (multiline_diff function)
Next, you will write a function called multiline_diff that takes two lists of single line strings. You may assume that the strings within the lists are all single lines. The function returns a tuple that indicates the line and index within that line where the first difference between the two lists occurs.  If the contents of the two lists are the same, the function should return the tuple (IDENTICAL, IDENTICAL).

# Problem 4: Getting lines from a file (get_file_lines)
Next, you will write a function called get_file_lines that takes a filename as input. You may assume that the input names a file that exists and is readable. The function returns a list of single line strings, where each element of the list is one line from the file. The strings within the returned list should not contain any newline or carriage return ("\n" or "\r") characters.
