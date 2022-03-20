"""
    Lists:
    ------
    1. len - displays number of elements
    2. append - inserts something at the end
    3. insert - inserts at the specified position
    4. remove - specify the item name to remove
    5. pop - removes the last item, and return what was removed
    6. reverse - reverse the list items
    7. sort - sorts in alpha order unless (reverse=True)
    8. sorted - to not change the original list
    9. min - returns mininum value of numbers
    10. max - returns maximum value of numbers
    11. sum - sum of all numbers
    12. index - pass element to find index of an element, if element not found, it will show value not found error.
    13. join - to make list items as string
    14. split - to make string to list
    
    Sets:
    -----
    1. intersection - intersection of items b/w two sets
    2. difference - shows the difference b/w two sets
    3. union - all items from both sets
    
    Facts about Lists:
    ------------------
    negative index - to get last item (-1)
    slicing - [start : end] here end won't be considered

    Facts about Tuples:
    -------------------
    tuples are immutable
    tuple value can be passed to other tuple, but values cannot be changed

    Facts about Set:
    ----------------
    sets doesn't care about order of values
    sets removes duplicates
    sets are more optimized when we do a value search

    Creating Empties:
    ------------------
    
    1. Empty Lists
    --------------
    empty_list = []
    empty_list = list()

    2. Empty Tuples
    ---------------
    empty_tuple = ()
    empty_typle = tuple()
    
    3. Empty Sets
    -------------
    empty_set = {} # This isn't right! It's a dict
    empty_set = set()

"""

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_tuple = ('History', 'Math', 'Physics', 'CompSci')
courses_set = {'History', 'Math', 'Physics', 'CompSci'}

math_bio = {'Maths','Physics','Chemistry','Botany','Zoology'}
math_cs = {'Maths','Physics','Chemistry','Computer Science'}

print(math_cs.difference(math_bio))