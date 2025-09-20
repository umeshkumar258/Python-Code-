
""" a = " a is binary file

email[umeshkumarjn143@gmail.com]
"""

f = open("file.txt","r")  # txt is extenation of file

# f()ile.txt = filename
# r = mode

data = f.read()
print(data)
f.close()

# text files = .txt,.c
# binary files = .jpg,.dat

# oprn is built in funtion it opens the file

'''
r': Read (default mode). Opens a file for reading.
'w': Write. Opens a file for writing. If the file exists, it truncates the file to zero length.
'a': Append. Opens a file for writing, but doesn’t truncate the file. Data is written at the end of the file.
'b': Binary. Used to read/write binary files (like images).
'x': Exclusive creation. If the file already exists, it throws an error.
't': Text (default mode). This is used for text files (it’s the default).
'r+': Read and Write. Opens a file for both reading and writing
'''
