numbers = [1, 2, 3, 5, 6]
n = 6
expected = n * (n + 1) // 2
actual = 0
for value in numbers:
    actual += value
print("Missing number:", expected - actual)
