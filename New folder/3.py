def ackerman(m, n, count=0):
    count += 1
    if m == 0:
        return n + 1, count
    elif m > 0 and n == 0:
        return ackerman(m - 1, 1, count + 1)
    elif m > 0 and n > 0:
        result, count = ackerman(m, n - 1, count)
        return ackerman(m - 1, result, count + 1)

result, count = ackerman(2, 3)
print(result, count)
