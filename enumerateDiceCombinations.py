# Creating a dictionary of all the possible combinations and their totals of two dice rolls

# Create dictionary
combos = {}

for d1 in range(1, 7):
    for d2 in range(1, 7):
        t = d1, d2  # At this point we have the combination

        # Now we want to see if d1 + d2 is a KEY in combos
        key = d1 + d2
        if key in combos:
            combos[key] += f"({t})"
        else:
            combos[key] = f"({t})"

print(combos)
