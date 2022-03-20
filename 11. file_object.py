"""
    File Operations
    ---------------
    r - read (default), 
    w - write, 
    a - append, 
    r+ - read/write
"""

""" Not a recommended way, as we need to remember closing file to avoid mem. leaks """
from tracemalloc import start


f = open('test.txt', 'r')
print(f.name)
f.close()

""" Opening file using context manager """

# Reading file - Way - 1
with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)

print(f.closed)
print(f.read())

# Reading file - Way - 2
with open('test.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents)

# Reading file - Way - 3
with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents, end='') # here end param is used to avoid new line
    f_contents = f.readline()
    print(f_contents)

# Reading file - Way - 4
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')

# Reading file - Way - 4
""" When we reach end of file, we're going to get empty string as response """
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0: # Loop until you find an empty string
        print(f_contents, end = '')
        f_contents = f.read(size_to_read)

""" Read File - Bonus Knowledge - Tell, Seek """
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end = '')
    print(f.tell()) # Tells the position of last read char
    print(f.seek(0)) # Moves the cursor to the given position
    f_contents = f.read(size_to_read)
    print(f_contents, end = '')
    print(f.tell())


# Write file - Way - 1
''' Create file with no content'''
with open('TestTnj.txt', 'w') as f:
    pass

# Write file - Way - 2
''' Write some content to a file '''
with open('TestTnj.txt', 'w') as f:
    f.write('Test_ing')
    f.seek(0) # Moves the cursor to the given position
    f.write('Ring') # This is overwritten in the current position

# Write file - Way - 3
''' Create file with no content'''
with open('test.txt', 'r') as rf:
    with open('tnj_info.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

''' Copy Image Files'''

# We get error if we try to write same way as text file
with open('Experiment/Focus.jpg', 'r') as rf:
    with open('Experiment/Focus_copy.jpg', 'w') as wf:
        for line in rf:
            wf.write(line)

# Picture files has to be read/write as binary
''' Line by line read - works'''
with open('Experiment/Focus.jpg', 'rb') as rf:
    with open('Experiment/Focus_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)

''' Read image files by chunk - Better '''
with open('Experiment/Focus.jpg', 'rb') as rf:
    with open('Experiment/FileSorting/Focus_copy_2.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)



""" Just a hands on experiment using above code """
def createFile(seqNumber):
    with open('Experiment/Focus.jpg', 'rb') as rf:
        with open(f'Experiment/FileSorting/Focus_copy_{seqNumber}.jpg', 'wb') as wf:
            chunk_size = 4096
            rf_chunk = rf.read(chunk_size)
            while len(rf_chunk) > 0:
                wf.write(rf_chunk)
                rf_chunk = rf.read(chunk_size)
for i in range(1, 11):
    createFile(i)