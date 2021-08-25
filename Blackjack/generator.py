"""
    Generator functions allows us to write a function that can send back a value and then later
    resume to pick up where it left off.
    Generator helps to consume less memory space i.e instead of storing things in a list.
    It is memory efficent and have to store things in a list.
    It doesnot hold every thing in a memory

"""
def create_squares(n):
    for x in range(n):
        yield x**2

print(list(create_squares(10)))
# Expected Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Or we can do also
for number in create_squares(10):
    print(number)


"""
        Let's again create a simple generator!!!
"""
def simple_gen():
    for x in range(3):
        yield x
for number in simple_gen():
    print(number)
g = simple_gen()
print(next(g))
#Output : 0
print(next(g))
# Output : 1
print(next(g))
# Output : 2

"""
    It;s remebering what previous one was and returning next value . It is not holding value
    in memory.
"""


