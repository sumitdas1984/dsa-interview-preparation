# arr = [4, 2, 14, 1, 3]
# print(reversed(arr))

people = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 25),
    ("David", 30)
]

sorted_people = sorted(people, key=lambda x: x[1])
print(sorted_people)
