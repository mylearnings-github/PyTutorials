'''
    Manually opening & closing file needs caution!
    If not done properly, it may lead to memory leak issues!

    Better way of opening file is to use Context Manager.
    It takes care of closing!
'''


""" Manual way """
f = open('test.txt', 'r')
file_contents = f.read()
f.close()


""" Using Context Manager """
with open('test.txt', 'r') as f:
    file_contents = f.read()


""" Some file operations - Demo """
words = file_contents.split(' ')
word_count = len(words)
print(word_count)