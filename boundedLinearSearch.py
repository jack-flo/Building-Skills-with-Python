# Using a bounded linear search to eliminate duplicate values from a list
sequence = [4, 7, 2, 9, 7, 13, 4, 18, 2, 25, 30, 13, 42, 18, 55]
distinctValues = []

for value in sequence:
    i = 0
    distinctValues.append(value)
    while distinctValues[i] != value:
        i += 1
    if i != len(distinctValues) - 1:
        del distinctValues[-1]

print(distinctValues)

# OR

sequence = [4, 7, 2, 9, 7, 13, 4, 18, 2, 25, 30, 13, 42, 18, 55]
distinctValues = []

for value in sequence:
    if value not in distinctValues:
        distinctValues.append(value)

print(distinctValues)
