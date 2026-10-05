numbers = [1, 2, 2, 3, 4, 4, 5]
unique = []
for n in numbers:
    if numbers.count(n) == 1:
        unique.append(n)
print(unique)
