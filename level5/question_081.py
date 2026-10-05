numbers = [4, 5, 1, 2, 1, 4, 5, 3]
seen = []
for n in numbers:
    if n in seen:
        print("First repeating:", n)
        break
    seen.append(n)
