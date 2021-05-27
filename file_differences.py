"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    lst = list()
    len1 = len(line1)
    len2 = len(line2)
    lst.append(len1)
    lst.append(len2)
    min_len = min(lst)
    if(len1 == len2):
        for ind_1 in range(len1):
            if(line1[ind_1] != line2[ind_1]):
                #print("both of the same length but has a diff")
                return(ind_1)

        #print("has no diff -1")
        return(IDENTICAL)
    if(len1 == 0 or len2 == 0):
        return(0)
    if(len1 != len2):
        if(min_len == len1):
            for ind_2 in range(len1):
                if(ind_2 != len1-1):
                    if(line1[ind_2] != line2[ind_2]):
                        #print("1st line is small")
                        return (ind_2)
                if(ind_2 == len1-1 and line1[ind_2] == line2[ind_2]):
                    ind_2 = ind_2+1
            #print("1st line is a prefix of 2nd line")
            return (ind_2)
        if(min_len == len2):
            for ind_3 in range(len2):
                if(ind_3 != len2-1):
                    if(line2[ind_3] != line1[ind_3]):
                        #print("2nd line is small")
                        return(ind_3)
                if(ind_3 == len2-1 and line2[ind_3] == line1[ind_3]):
                    #print("2nd line is a prefix of 1st line")
                    ind_3 = ind_3+1
            #print("2nd line is a prefix of 1st line")
            return (ind_3)



# print(singleline_diff('I am lily', 'I am james'))
# print(singleline_diff('I am lily', 'I am lilye'))
# print(singleline_diff('I am lily', 'I am lily'))
# print(singleline_diff('I am lily', 'I am lely'))
# print(singleline_diff('I am lily', 'I am snape'))
# print(singleline_diff('I am snape', 'I am lily'))

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    lst = list()
    len1 = len(line1)
    len2 = len(line2)
    lst.append(len1)
    lst.append(len2)
    min_len = min(lst)
    if '\n' in line1 or '\r' in line1:
        return("")
    elif '\n' in line2 or '\r' in line2:
        return("")
    elif(idx < 0 or idx > min_len):
        return("")
    else:
        return(line1 + "\n" + "=" * idx + "^" + "\n" + line2 + "\n")

# line1='abc'
# line2='abd'
# idx=singleline_diff(line1, line2)
# singleline_diff_format(line1, line2, idx)

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    len1 = len(lines1)
    len2 = len(lines2)
    min_len = min(len1, len2)
    if(len1 == 0 and len2 == 0):
        return(IDENTICAL, IDENTICAL)
    if(len1 == 0 or len2 == 0):
        return(0, 0)
    for index in range(min_len):
        idx = singleline_diff(lines1[index], lines2[index])
        if(idx == IDENTICAL and index == min_len-1 and len1 == len2):
            return(IDENTICAL, IDENTICAL)
        elif(idx == IDENTICAL and index == min_len-1):
            return(min_len, 0)
        elif(idx == IDENTICAL):
            continue
        else:
            return(index, idx)

#     if(len1 == len2):
#         for index in range(len1):
#             if(lines1[index] != lines2[index]):
#                 line_index = index
#             else:
#                 if(index == len1-1):
#                     line_index = IDENTICAL
#         return(line_index, singleline_diff(lines1[line_index], lines2[line_index]))
#     if(len1 != len2):
#         for index2 in range(min_len):
#             if(lines1[index2] != lines2[index2]):
#                 line_index = min_len
#                 if(index2 == min_len-1):
#                     return(line_index, singleline_diff(lines1[index2], lines2[index2])
#
#     return (IDENTICAL, IDENTICAL)
#
#
def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    with open(filename) as file:
        content = file.read().splitlines()
    return(content)


# def file_diff_format(filename1, filename2):
#     """
#     Inputs:
#       filename1 - name of first file
#       filename2 - name of second file
#     Output:
#       Returns a four line string showing the location of the first
#       difference between the two files named by the inputs.
#
#       If the files are identical, the function instead returns the
#       string "No differences\n".
#
#   If either file does not exist or is not readable, then the
#   behavior of this function is undefined.
# """
# return ""
