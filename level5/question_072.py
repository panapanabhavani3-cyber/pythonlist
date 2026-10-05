numbers = [1, 2, 2, 3, 1, 4, 3]
duplicates = []
for n in numbers:
    if numbers.count(n) > 1 and n not in duplicates:
        duplicates.append(n)
print(duplicates)
