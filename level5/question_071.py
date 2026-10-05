numbers = [1, 2, 2, 3, 1, 4, 3]
result = []
for n in numbers:
    if n not in result:
        result.append(n)
print(result)
