"""
You have an N-element tuple or sequence that you would like to unpack into a collection
of N variables.
"""

p = (4, 5)
x, y = p

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
name1, shares1, price1, (year, mon, day) = data

# string
s = 'Hello'
a, b, c, d, e = s

# discard certain values
_, shares2, price2, _ = data
