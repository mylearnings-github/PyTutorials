import memory_profiler as mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci','Arts','Business']

print(f'Memory (Before): {mem_profile.memory_usage()}MB')

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(num_people):    
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

""" Test People List """

t1 = time.time()
people = people_list(1000000)
t2 = time.time()

""" Test People Generator """

# t1 = time.time()
# people = people_generator(1000000)
# # people = list(people_generator(1000000)) # We lose our performance when we convert the generator result to the list
# t2 = time.time()

print(f'Memory (After): {mem_profile.memory_usage()}MB')
print(f'Took {t2-t1} Seconds')