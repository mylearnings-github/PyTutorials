"""
    Try/Except Blocks for Error Handling
"""


try:    
    #f = open('test.txt')
    f = open('Experiment/corrupt_file.txt')
    if f.name == 'Experiment/corrupt_file.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!', e)
else:
    ''' else clause only runs when there is no exception '''
    print(f.read())
    f.close()
finally:
    ''' no matter you had an exception or not, finally will run at the end '''
    print('Executing Finally...')