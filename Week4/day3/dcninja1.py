def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n


numbers = list(range(100))

for i in numbers:
  print(i, perfect_number(i))
