"""
You need to unpack N elements from an iterable, but the iterable may be longer than N
elements, causing a “too many values to unpack” exception.
"""
import numpy as np


def drop_first_last(grades):
    first, *middle, last = grades
    return np.mean(middle)


grades = [1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10]
avg = drop_first_last(grades)

print("Average:", avg)

# As another use case, suppose you have user records that consist of a name and email
# address, followed by an arbitrary number of phone numbers. You could unpack the
# records like this:

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name, email, phone_numbers)

user_record = ('Dave', 'dave@example.com', '847-555-1212')
*personal_data, phone_number = user_record
print(personal_data, phone_number)

# It is worth noting that the star syntax can be especially useful when iterating over a
# sequence of tuples of varying length. For example, perhaps a sequence of tagged tuples:

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
